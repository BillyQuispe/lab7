from kafka import KafkaProducer
import json
import time
import random

# Cargar los datos musicales desde el archivo JSON
with open('music_data.json') as f:
    music_data_list = json.load(f)

# Configuración del productor de Kafka
producer = KafkaProducer(
    bootstrap_servers='ec2-98-82-15-48.compute-1.amazonaws.com:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),
    max_in_flight_requests_per_connection=1,  # Permitir solo un mensaje en vuelo por conexión
    linger_ms=0,  # Sin retraso en la acumulación
    batch_size=32768,  # Tamaño máximo del lote en bytes
    compression_type='gzip'  # Compresión gzip para los mensajes
)

while True:
    # Seleccionar un artista aleatorio de la lista cargada
    artist_data = random.choice(music_data_list)
    producer.send('music_topic', value=artist_data)
    print(f"Sent: {artist_data}")
    time.sleep(3)  # Enviar un mensaje cada 3 segundos
