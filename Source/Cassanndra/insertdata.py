from cassandra.cluster import Cluster
import os
from dotenv import load_dotenv

load_dotenv()
cassandra_host = os.getenv('IP_CASSANDRA')
print(cassandra_host)

# Connect to the Cassandra cluster
cluster = Cluster([cassandra_host], port=9042)
session = cluster.connect()

# Create a keyspace if it doesn't exist
session.execute("CREATE KEYSPACE IF NOT EXISTS my_keyspace WITH replication = {'class':'SimpleStrategy', 'replication_factor':3}")

# Use the keyspace
session.set_keyspace('my_keyspace')


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


session.execute("DROP TABLE IF EXISTS review")

# Create the updated products table
session.execute("""
    CREATE TABLE review (
        id text,
        id_product text,
        content text,
        star int,
        tilte text,
        status  text,
        PRIMARY KEY (id)
    )
""")

# Đóng kết nối
session.shutdown()
cluster.shutdown()
