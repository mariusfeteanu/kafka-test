import java.time.Duration
import java.util.Properties
import java.util.regex.Pattern

import org.apache.kafka.streams.{KafkaStreams, StreamsConfig}
import org.apache.kafka.streams.scala.kstream._
import org.apache.kafka.streams.scala.StreamsBuilder

object WordCount extends App {

  import org.apache.kafka.streams.scala.Serdes._
  import org.apache.kafka.streams.scala.ImplicitConversions._

  val bootstrapServers = args(0)
  println(s"Starting print app, using $bootstrapServers")

  val config: Properties = {
    val p = new Properties()
    p.put(StreamsConfig.APPLICATION_ID_CONFIG, "word_count")
    p.put(StreamsConfig.BOOTSTRAP_SERVERS_CONFIG, bootstrapServers)
    p
  }


  val builder = new StreamsBuilder
  val source: KStream[String, String] = builder.stream[String, String]("test_topic")

  val pattern = Pattern.compile("\\W+")

  val counts = source
      .flatMapValues(value => pattern.split(value))
      .map((key, value) => (value, value))
      .filter((key, value) => value !=  "the")
      .groupByKey
      .count()
      .mapValues(value => value.toLong)
      .toStream

  counts.to("wordcount_test_topic")

  val topology = builder.build()
  val streams = new KafkaStreams(topology, config)

  streams.start()


  // Add shutdown hook to respond to SIGTERM and gracefully close Kafka Streams
  sys.ShutdownHookThread {
    streams.close(Duration.ofSeconds(10))
  }

}
