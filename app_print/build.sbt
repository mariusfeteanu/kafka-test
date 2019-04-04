name := "app-print"
version := "1.0"
scalaVersion := "2.12.0"

// libraryDependencies += "org.apache.kafka" % "kafka-streams" % "2.2.0"
libraryDependencies += "org.apache.kafka" %% "kafka-streams-scala" % "2.2.0"


mainClass in assembly := Some("AppPrint")
