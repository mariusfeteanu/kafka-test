### Build an JVM app
(cd app_print; sbt)

### JVM apps
docker-compose run apps word-count

### Python apps
docker-compose run faust word_count.main
