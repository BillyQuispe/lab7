from kafka import KafkaProducer
import json
import boto3
import time
import random

# Configuración de AWS S3
S3_BUCKET = 'voting-app-music-data'
S3_KEY = 'data.json'

# Inicializar cliente de S3
s3 = boto3.client('s3')

# Configuración del productor de Kafka
producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Leer datos desde S3
response = s3.get_object(Bucket=S3_BUCKET, Key=S3_KEY)
music_data = json.loads(response['Body'].read().decode('utf-8'))

# Enviar datos a Kafka
for song in music_data:
    producer.send('top_music', song)
    print(f'Sent: {song}')
    time.sleep(1)  # Esperar un segundo antes de enviar el siguiente dato

producer.flush()  # Asegúrate de enviar todos los mensajes
