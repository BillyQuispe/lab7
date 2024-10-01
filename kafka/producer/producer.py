from kafka import KafkaProducer
import time
import json
import random

producer = KafkaProducer(
    bootstrap_servers='ec2-44-201-171-184.compute-1.amazonaws.com:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

while True:
    data = {
        'timestamp': time.time(),
        'value': random.randint(1, 100)
    }
    print(f"Producing data: {data}")
    producer.send('realtime-analytics', value=data)
    time.sleep(1)
