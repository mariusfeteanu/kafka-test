import java.time.Duration
import java.util.Properties

import org.apache.kafka.streams.{KafkaStreams, StreamsConfig}
import org.apache.kafka.streams.StreamsBuilder

object MapFunctionScalaExample extends App {

  // import org.apache.kafka.streams.scala.Serdes._
  // import org.apache.kafka.streams.scala.ImplicitConversions._

  val config: Properties = {
    val p = new Properties()
    p.put(StreamsConfig.APPLICATION_ID_CONFIG, "app_print")
    val bootstrapServers = args(0)
    p.put(StreamsConfig.BOOTSTRAP_SERVERS_CONFIG, bootstrapServers)
    p
  }

  val builder = new StreamsBuilder
  // val textLines: KStream[Array[Byte], String] = builder.stream[Array[Byte], String]("test_topic")

  // Variant 1: using `mapValues`
  // val uppercasedWithMapValues: KStream[Array[Byte], String] = textLines.mapValues(_.toUpperCase())
  // uppercasedWithMapValues.to("UppercasedTextLinesTopic")

  // Variant 2: using `map`, modify both key and value
  // val originalAndUppercased: KStream[String, String] = textLines.map((_, value) => (value, value.toUpperCase()))

  // Write the results to a new Kafka topic "OriginalAndUppercasedTopic".
  // originalAndUppercased.to("OriginalAndUppercasedTopic")

  val streams: KafkaStreams = new KafkaStreams(builder.build(), config)
  streams.start()

  sys.ShutdownHookThread {
    streams.close(Duration.ofSeconds(10))
  }

}
