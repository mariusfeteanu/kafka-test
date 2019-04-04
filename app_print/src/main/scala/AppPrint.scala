import java.time.Duration
import java.util.Properties

import org.apache.kafka.streams.{KafkaStreams, StreamsConfig}
// import org.apache.kafka.streams.StreamsBuilder
import org.apache.kafka.streams.scala.kstream._
import org.apache.kafka.streams.scala.StreamsBuilder

object MapFunctionScalaExample extends App {

  import org.apache.kafka.streams.scala.Serdes._
  import org.apache.kafka.streams.scala.ImplicitConversions._

  val config: Properties = {
    val p = new Properties()
    p.put(StreamsConfig.APPLICATION_ID_CONFIG, "app_print")
    val bootstrapServers = args(0)
    p.put(StreamsConfig.BOOTSTRAP_SERVERS_CONFIG, bootstrapServers)
    p
  }

  val builder = new StreamsBuilder
  val textLines: KStream[String, String] = builder.stream[String, String]("test_topic")

  textLines.peek(
    (key, value) => println(s"key: $key, value: $value")
  )

  val streams: KafkaStreams = new KafkaStreams(builder.build(), config)
  streams.start()

  sys.ShutdownHookThread {
    streams.close(Duration.ofSeconds(10))
  }

}
