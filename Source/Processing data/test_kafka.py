from confluent_kafka import Producer, Consumer, KafkaError
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

# Đăng ký topic để tiêu thụ tin nhắn
topic = 'quickstart'
consumer.subscribe([topic])

# Tạo producer
producer = Producer(producer_config)

# Gửi tin nhắn tới topic
message = 'Hello, Kafka!'

producer.produce(topic, message.encode('utf-8'))

# Chờ tin nhắn được gửi thành công
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
    print('Nhận tin nhắn: {}'.format(message.value().decode('utf-8')))

# Đóng consumer khi kết thúc
consumer.close()