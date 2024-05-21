from cassandra.cluster import Cluster
import os
from dotenv import load_dotenv

load_dotenv()
cassandra_host = os.getenv('IP_CASSANDRA')

# Connect to the Cassandra cluster
cluster = Cluster([cassandra_host], port=9042)
session = cluster.connect()
session.set_keyspace('my_keyspace')

# Execute a SELECT query
query = "SELECT * FROM product_information"
result = session.execute(query)

# Print the results
for row in result:
    print(row)

session.shutdown()
cluster.shutdown()