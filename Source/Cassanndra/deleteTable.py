from cassandra.cluster import Cluster
import os
from dotenv import load_dotenv

load_dotenv()
cassandra_host = os.getenv('IP_CASSANDRA')

# Connect to the Cassandra cluster
cluster = Cluster([cassandra_host], port=30042)
session = cluster.connect()

# Use the keyspace
session.set_keyspace('my_keyspace')

# Drop the table if it exists
session.execute("DROP TABLE IF EXISTS id_table")

# Close the session and cluster connection
session.shutdown()
cluster.shutdown()
