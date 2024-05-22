from cassandra.cluster import Cluster
import os
from dotenv import load_dotenv
import json

# Load the environment variables
load_dotenv()
class CassandraConnector:
    def __init__(self):
        self.ip_cassandra = os.getenv('IP_CASSANDRA')
        self.port_cassandra = os.getenv('PORT_CASSANDRA')
        self.cluster = Cluster([self.ip_cassandra],port= self.port_cassandra)  # Replace 'localhost' with the IP address of your Cassandra cluster
        self.session = self.cluster.connect()
        self.session.set_keyspace('my_keyspace')

    def query(self, query):
        rows=self.session.execute(query)
        result = [row._asdict() for row in rows]
        return result
    
    def insert(self, query):
        self.session.execute(query)
        
    def close(self):
        self.session.shutdown()
        self.cluster.shutdown()
