from kafka import KafkaProducer
import json
import random

# Configuración del productor de Kafka
producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Generar y enviar 50 datos
for i in range(50):
    music_data = {
        'artist': f'Artist {random.randint(1, 100)}',
        'title': f'Song {random.randint(1, 100)}'
    }
    producer.send('top_music', music_data)
    print(f'Sent: {music_data}')

producer.flush()  # Asegúrate de enviar todos los mensajes
