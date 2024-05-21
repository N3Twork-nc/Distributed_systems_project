import requests
import json
from kafka import KafkaProducer
import os
from dotenv import load_dotenv

load_dotenv() 

bootstrap_servers = os.getenv("BOOTSTRAP_SERVERS")

page_url = "https://tiki.vn/api/personalish/v1/blocks/listings?limit=40&include=advertisement&aggregations=2&version=home-persionalized&trackity_id=680c18ed-7be4-1045-443b-c3b0e7083ee1&category=8322&page={}&urlKey=nha-sach-tiki"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}

producer = KafkaProducer(
    bootstrap_servers=bootstrap_servers,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def crawl_product_id():
    i = 1
    while True:
        print("Crawl page: ", i)
        response = requests.get(page_url.format(i), headers=headers)
        
        if response.status_code != 200:
            break

        products = json.loads(response.text)["data"]

        if len(products) == 0:
            break

        for product in products:
            product_id = str(product["id"])
            print("Product ID: ", product_id)
            producer.send('id', {'product_id': product_id})

        i += 1

if __name__ == "__main__":
    crawl_product_id()
