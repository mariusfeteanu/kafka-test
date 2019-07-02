all:
	echo "don't know how to make all"

clean:
	rm -rf data/kafka/1/*
	rm -rf data/kafka/2/*
	rm -rf data/kafka/3/*
	rm -rf data/kafka/4/*
	rm -rf data/kafka/5/*
	rm -rf data/zookeeper/1/version-2/*
	rm -rf data/zookeeper/2/version-2/*
	rm -rf data/zookeeper/3/version-2/*
