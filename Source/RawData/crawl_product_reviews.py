import requests
import json
from kafka import KafkaProducer, KafkaConsumer

review_url_template = "https://tiki.vn/api/v2/reviews?limit=1&include=comments&page={}&spid=50685549&product_id={}&seller_id=1"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
}

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

consumer = KafkaConsumer(
    'id',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    group_id='product-review-group',
    value_deserializer=lambda v: json.loads(v.decode('utf-8'))
)

def crawl_reviews(product_id):
    page = 1
    reviews = []
    while True:
        print(page)
        review_url = review_url_template.format(page, product_id)
        response = requests.get(review_url, headers=headers)
        if response.status_code == 200:
            if (page>50):print(response.json())
            review_data = response.json()
            if not review_data['data']:
                break
            reviews.extend(review_data['data'])
            page += 1
        else:
            print("Failed to crawl reviews: ", response.status_code)
            break
    return reviews

if __name__ == "__main__":
    for message in consumer:
        product_id = message.value['product_id']
        print(product_id)
        reviews = crawl_reviews(product_id)
        print(reviews)
        if reviews:
            producer.send('reviews', {'product_id': product_id, 'reviews': reviews})
