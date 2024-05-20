from cassandra.cluster import Cluster
import os
from dotenv import load_dotenv
from kafka import KafkaConsumer
import json

load_dotenv()

# Kafka configuration
bootstrap_servers = os.getenv("BOOTSTRAP_SERVERS")

# Cassandra configuration
cassandra_host = os.getenv('IP_CASSANDRA')

# Kafka Consumer setup
consumer = KafkaConsumer(
    'id',
    bootstrap_servers=bootstrap_servers,
    auto_offset_reset='earliest',
    value_deserializer=lambda v: json.loads(v.decode('utf-8'))
)

# Connect to the Cassandra cluster
cluster = Cluster([cassandra_host], port=30042)
session = cluster.connect()

# Create a keyspace if it doesn't exist
session.execute("CREATE KEYSPACE IF NOT EXISTS my_keyspace WITH replication = {'class':'SimpleStrategy', 'replication_factor':1}")

# Use the keyspace
session.set_keyspace('my_keyspace')

# Create a table if it doesn't exist
session.execute("CREATE TABLE IF NOT EXISTS id_table (id UUID PRIMARY KEY, product_id TEXT)")

# Function to check if a product_id exists in the table
def product_id_exists(product_id):
    query = "SELECT COUNT(*) FROM id_table WHERE product_id = %s ALLOW FILTERING"
    result = session.execute(query, (product_id,))
    count = result.one()[0]
    return count > 0

# Insert data into the table
for message in consumer:
    product_id = message.value['product_id']
    if not product_id_exists(product_id):
        session.execute("INSERT INTO id_table (id, product_id) VALUES (uuid(), %s)", (product_id,))

# Close the session and cluster connection
session.shutdown()
cluster.shutdown()
