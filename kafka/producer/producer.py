from kafka import KafkaProducer
import json
import time
import random

# Cargar los datos musicales desde el archivo JSON
with open('music_data.json') as f:
    music_data_list = json.load(f)

# Configuración del productor de Kafka
producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

while True:
    # Selecciona un artista aleatorio de la lista cargada
    artist_data = random.choice(music_data_list)
    producer.send('music_topic', value=artist_data)
    print(f"Sent: {artist_data}")
    time.sleep(5)  # Enviar un mensaje cada 5 segundos
