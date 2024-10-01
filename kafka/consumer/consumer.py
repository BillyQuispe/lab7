from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'realtime-analytics',
    bootstrap_servers='ec2-98-81-255-236.compute-1.amazonaws.com:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

for message in consumer:
    print(f"Consumed data: {message.value}")
