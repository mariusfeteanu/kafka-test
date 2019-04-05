import java.time.Duration
import java.util.Properties

import org.apache.kafka.streams.{KafkaStreams, StreamsConfig}
// import org.apache.kafka.streams.StreamsBuilder
import org.apache.kafka.streams.scala.kstream._
import org.apache.kafka.streams.scala.StreamsBuilder

// https://github.com/confluentinc/kafka-streams-examples/blob/5.2.1-post/src/main/scala/io/confluent/examples/streams/MapFunctionScalaExample.scala
object AppPrint extends App {

  import org.apache.kafka.streams.scala.Serdes._
  import org.apache.kafka.streams.scala.ImplicitConversions._

  val bootstrapServers = args(0)
  println(s"Starting print app, using $bootstrapServers")

  val config: Properties = {
    val p = new Properties()
    p.put(StreamsConfig.APPLICATION_ID_CONFIG, "app_print")
    p.put(StreamsConfig.BOOTSTRAP_SERVERS_CONFIG, bootstrapServers)
    p
  }


  val builder = new StreamsBuilder
  val textLines: KStream[String, String] = builder.stream[String, String]("test_topic")

  textLines.peek(
    (key, value) => println(s"key: $key, value: $value")
  )

  val wordCounts: KTable[String, Long] = textLines
    .flatMapValues(textLine => textLine.toLowerCase.split("\\W+"))
    .groupBy((_, word) => word)
    .count()
  wordCounts.toStream.to("test_topic_wordcount")

  val streams: KafkaStreams = new KafkaStreams(builder.build(), config)

  streams.cleanUp() // Just a test!
  streams.start()


  // Add shutdown hook to respond to SIGTERM and gracefully close Kafka Streams
  sys.ShutdownHookThread {
   streams.close(Duration.ofSeconds(10))
 }

}
