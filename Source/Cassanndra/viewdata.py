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
query = "SELECT * FROM id_table"
result = session.execute(query)

# Collect the results into a list of dictionaries
data = []
for row in result:
    data.append({
        'product_id': row.product_id
    })

# Get the current directory
current_directory = os.path.dirname(os.path.abspath(__file__))

# Write the data to a JSON file in the same directory as viewdata.py
data_file_path = os.path.join(current_directory, 'data.json')
with open(data_file_path, 'w') as f:
    json.dump(data, f)

# Execute a SELECT COUNT query to get the number of rows in id_table
count_query = "SELECT COUNT(*) FROM id_table"
count_result = session.execute(count_query)

# Get the count from the result
row_count = count_result.one()[0]  # Assuming the count is the first column in the result
print(f"Number of rows in id_table: {row_count}")
