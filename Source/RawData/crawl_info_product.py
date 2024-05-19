import requests
import json
from kafka import KafkaProducer, KafkaConsumer
import os
from dotenv import load_dotenv, dotenv_values 

load_dotenv() 

bootstrap_servers = os.getenv("BOOTSTRAP_SERVERS")
group_id = os.getenv("GROUP_ID_INFO")

product_url_template = "https://tiki.vn/api/v2/products/{}?platform=web&spid={}&version=3"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
}

producer = KafkaProducer(
    bootstrap_servers=bootstrap_servers,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

consumer = KafkaConsumer(
    'id',
    bootstrap_servers=bootstrap_servers,
    auto_offset_reset='earliest',
    group_id=group_id,
    value_deserializer=lambda v: json.loads(v.decode('utf-8'))
)

def crawl_product(product_id):
    product_url = product_url_template.format(product_id, product_id)
    response = requests.get(product_url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to crawl product: ", response.status_code)
        return None

if __name__ == "__main__":
    for message in consumer:
        product_id = message.value['product_id']
        product_info = crawl_product(product_id)
        if product_info:
            producer.send('info', product_info)
