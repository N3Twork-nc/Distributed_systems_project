from confluent_kafka import Producer, Consumer, KafkaError
import json
from crawl_product_id import crawl_product_id
from crawl_product_reviews import crawl_reviews
from crawl_info_product import crawl_product

# Cấu hình cho producer
producer_config = {
    'bootstrap.servers': 'localhost:9092',  # Danh sách các Kafka broker
    'client.id': '12121'  # ID của producer
}

# Cấu hình cho consumer
consumer_config = {
    'bootstrap.servers': 'localhost:9092',  # Danh sách các Kafka broker
    'group.id': '121212',  # ID của consumer group
    'auto.offset.reset': 'earliest'  # Offset sẽ được reset về đầu partition nếu không có offset đã lưu trữ
}

# Tạo consumer
consumer = Consumer(consumer_config)

# Đăng ký để tiêu thụ tin nhắn từ tất cả các topic
consumer.subscribe(['info', 'reviews', 'id'])

# Tạo producer
producer = Producer(producer_config)

# Lấy danh sách product_id từ topic 'id'
product_list, _ = crawl_product_id()

# Lặp qua từng product_id
for product_id in product_list:
    # Crawl thông tin sản phẩm và gửi vào topic 'info'
    product_info = crawl_product(product_id)
    if product_info:
        producer.produce('info', json.dumps(product_info).encode('utf-8'))
        producer.flush()

    # Crawl nhận xét sản phẩm và gửi vào topic 'reviews'
    reviews = crawl_reviews(product_id)
    if reviews:
        producer.produce('reviews', json.dumps(reviews).encode('utf-8'))
        producer.flush()

# Lặp để tiếp tục nhận tin nhắn
while True:
    message = consumer.poll(1.0)

    if message is None:
        continue

    if message.error():
        if message.error().code() == KafkaError._PARTITION_EOF:
            # Đã đến cuối partition, không có tin nhắn mới để tiếp tục nhận
            continue
        else:
            # Xảy ra lỗi khác
            print('Lỗi khi nhận tin nhắn: {}'.format(message.error().str()))
            continue

    # Xử lý tin nhắn nhận được
    print('Nhận tin nhắn từ topic {}: {}'.format(message.topic(), message.value().decode('utf-8')))

# Đóng consumer khi kết thúc
consumer.close()
