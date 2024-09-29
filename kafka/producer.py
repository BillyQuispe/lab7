from kafka import KafkaProducer
import json

# Cargar los datos musicales desde el archivo JSON
with open('music_data.json') as f:
    music_data_list = json.load(f)

# Configuración del productor de Kafka
producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Generar y enviar datos
for music_data in music_data_list:
    producer.send('top_music', music_data)
    print(f'Sent: {music_data}')

producer.flush()  # Asegúrate de enviar todos los mensajes
