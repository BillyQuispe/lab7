from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'realtime-analytics',
    bootstrap_servers='ec2-18-206-251-20.compute-1.amazonaws.com:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

for message in consumer:
    print(f"Consumed data: {message.value}")
