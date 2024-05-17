from confluent_kafka import Producer, Consumer, KafkaError
import json
from crawl_product_id import crawl_product_id
from crawl_info_product import crawl_product
from crawl_product_reviews import crawl_reviews

producer_config = {
    'bootstrap.servers': 'localhost:9092',
    'client.id': '12121'
}

consumer_config = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': '121212',
    'auto.offset.reset': 'earliest'
}

producer = Producer(producer_config)
consumer = Consumer(consumer_config)
consumer.subscribe(['id', 'info', 'reviews'])

if __name__ == "__main__":
    # Chạy crawl_product_id để gửi ID sản phẩm vào Kafka topic 'id'
    crawl_product_id()
    
    while True:
        message = consumer.poll(1.0)  # Poll with a timeout of 1 second

        if message is None:
            continue

        if message.error():
            if message.error().code() == KafkaError._PARTITION_EOF:
                # End of partition event
                continue
            else:
                # Error
                print(f"Error: {message.error()}")
                continue

        topic = message.topic()
        msg_value = json.loads(message.value().decode('utf-8'))

        if topic == 'id':
            product_id = msg_value['product_id']
            
            # Crawl product info
            product_info = crawl_product(product_id)
            if product_info:
                producer.produce('info', json.dumps(product_info).encode('utf-8'))
                producer.flush()
            
            # Crawl product reviews
            reviews = crawl_reviews(product_id)
            if reviews:
                producer.produce('reviews', json.dumps(reviews).encode('utf-8'))
                producer.flush()
        
        elif topic == 'info':
            product_info = msg_value
            print(f"Product info received: {product_info}")
        
        elif topic == 'reviews':
            reviews = msg_value
            print(f"Reviews received: {reviews}")

consumer.close()
