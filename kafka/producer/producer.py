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

# Envía cada elemento de la lista en un bucle
for item in music_data:
    producer.send('music_topic', value=item)
    print(f"Sent: {item}")
    time.sleep(5)   # Asegúrate de enviar todos los mensajes
