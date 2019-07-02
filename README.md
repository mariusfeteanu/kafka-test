### Build an JVM app
(cd app_print; sbt)

### JVM apps
docker-compose run apps word-count

### Python apps
docker-compose run faust word_count.main

## Inovation day demo

If copying code from main repo:
  - remove () in table names
  - leave app spec alone or modify to use the actual kafka one

docker-compose run faust inno.main

docker-compose run --entrypoint=bash faust
