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
table_name = 'product_information'
session.execute("DROP TABLE IF EXISTS product_information")

# Create the updated products table
session.execute("""
    CREATE TABLE product_information (
        id text,
        name text,
        short_url text,
        thumbnail_url text,
        discount_rate int,
        specifications text,
        all_time_quantity_sold int,
        rating_average double,
        review_count int,
        categories text,
        PRIMARY KEY (id)
    )
""")

print("Table 'products' created successfully.")

# Đóng kết nối
session.shutdown()
cluster.shutdown()
