from cassandra.cluster import Cluster
import os
from dotenv import load_dotenv
import json

load_dotenv()
cassandra_host = os.getenv('IP_CASSANDRA')

# Connect to the Cassandra cluster
cluster = Cluster([cassandra_host], port=30042)
session = cluster.connect()
session.set_keyspace('my_keyspace')

# Execute a SELECT query
query = "SELECT * FROM product_information"
result = session.execute(query)

# Collect the results into a list of dictionaries
data = []
for row in result:
    print(row)

session.shutdown()
cluster.shutdown()