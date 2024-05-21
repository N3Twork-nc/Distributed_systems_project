import requests
import json
from kafka import KafkaProducer, KafkaConsumer
import os
from urllib.parse import quote
from dotenv import load_dotenv

load_dotenv()

bootstrap_servers = os.getenv("BOOTSTRAP_SERVERS")
group_id = os.getenv("GROUP_ID_REVIEWS")

review_url_template = "https://tiki.vn/api/v2/reviews?limit=1&include=comments&page={}&spid=50685549&product_id={}&seller_id=1"
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

def crawl_reviews(product_id):
    page = 1
    while True:
        review_url = review_url_template.format(page, quote(str(product_id)))
        response = requests.get(review_url, headers=headers)
        if response.status_code == 200:
            if (page > 50):
                print(response.json())
            review_data = response.json()
            if not review_data['data']:
                break
            for review in review_data['data']:
                try:
                    # Gửi từng bình luận lên Kafka
                    producer.send('reviews', {'product_id': product_id, 'review': review})
                    producer.flush()
                except Exception as e:
                    print(f"Error while sending review to Kafka for product {product_id}: {e}")
            page += 1
        else:
            print("Failed to crawl reviews: ", response.status_code)
            break

if __name__ == "__main__":
    for message in consumer:
        product_id = message.value['product_id']
        crawl_reviews(product_id)
