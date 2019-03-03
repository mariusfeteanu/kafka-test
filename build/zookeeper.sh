cd /root
wget -q http://mirrors.ukfast.co.uk/sites/ftp.apache.org/zookeeper/stable/zookeeper-3.4.12.tar.gz
tar -zxf zookeeper-3.4.12.tar.gz
mv zookeeper-3.4.12 /usr/local/zookeeper
mkdir -p /var/lib/zookeeper

cat > /usr/local/zookeeper/conf/zoo.cfg << EOF
tickTime=2000
dataDir=/var/lib/zookeeper
clientPort=2181
EOF

