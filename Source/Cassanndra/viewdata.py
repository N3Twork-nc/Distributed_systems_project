from cassandra.cluster import Cluster
import os
from dotenv import load_dotenv

load_dotenv()
cassandra_host = os.getenv('IP_CASSANDRA')

# Connect to the Cassandra cluster
cluster = Cluster([cassandra_host], port=30042)
session = cluster.connect()
session.set_keyspace('my_keyspace')

# Execute a SELECT query
query = "SELECT * FROM id_table"
result = session.execute(query)

# Print the results
for row in result:
    print(row)

# Execute a SELECT COUNT query to get the number of rows in id_table
count_query = "SELECT COUNT(*) FROM id_table"
count_result = session.execute(count_query)

# Get the count from the result
row_count = count_result.one()[0]  # Assuming the count is the first column in the result
print(f"Number of rows in id_table: {row_count}")