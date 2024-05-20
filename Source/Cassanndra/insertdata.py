from cassandra.cluster import Cluster
import os
from dotenv import load_dotenv

load_dotenv()
cassandra_host = os.getenv('IP_CASSANDRA')

# Connect to the Cassandra cluster
cluster = Cluster([cassandra_host], port=30042)
session = cluster.connect()

# Create a keyspace if it doesn't exist
session.execute("CREATE KEYSPACE IF NOT EXISTS my_keyspace WITH replication = {'class':'SimpleStrategy', 'replication_factor':1}")

# Use the keyspace
session.set_keyspace('my_keyspace')

# Create a table if it doesn't exist
session.execute("CREATE TABLE IF NOT EXISTS my_table (id UUID PRIMARY KEY, name TEXT)")

# Insert data into the table
session.execute("INSERT INTO my_table (id, name) VALUES (uuid(), 'John Doe')")

# Close the session and cluster connection
session.shutdown()
cluster.shutdown()