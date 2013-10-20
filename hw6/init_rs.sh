#!/bin/bash
killall mongod
# remove the directories
rm -rf /data/rs1 /data/rs2 /data/rs3
# create them
mkdir -p /data/rs1 /data/rs2 /data/rs3

# start a replica set
mongod --replSet m101 --logpath "1.log" --dbpath /data/rs1 --port 27017 --smallfiles --oplogSize 64 --fork
mongod --replSet m101 --logpath "2.log" --dbpath /data/rs2 --port 27018 --smallfiles --oplogSize 64 --fork
mongod --replSet m101 --logpath "3.log" --dbpath /data/rs3 --port 27019 --smallfiles --oplogSize 64 --fork


sleep 10
# connect to one server and initiate the set
mongo --port 27017 << 'EOF'
config = { _id: "m101", members:[
          { _id : 0, host : "localhost:27017"},
          { _id : 1, host : "localhost:27018"},
          { _id : 2, host : "localhost:27019"} ]
};
rs.initiate(config);
EOF


# the state of replication.
rs.status()
