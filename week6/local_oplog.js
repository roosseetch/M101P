use local
show collections
db.oplog.rs.find()

mongo --port 27018
ps -ef | grep mongo
# Now kill PRIMARY SERVER process by it PID
# So we can Look How Long it will take to Vote New PRIMARY
kill 6463
