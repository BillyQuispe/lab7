from kafka import KafkaConsumer
import json

# Configuración del consumidor
consumer = KafkaConsumer(
    'music_topic',  # Nombre del tema al que está suscrito
    bootstrap_servers='kafka:9092',  # Dirección del broker Kafka
    auto_offset_reset='earliest',  # Comenzar desde el inicio del tema
    enable_auto_commit=True,  # Confirmar automáticamente los mensajes
    group_id='music_group',  # ID del grupo de consumidores
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))  # Deserializar el mensaje en JSON
)

# Procesar mensajes
for message in consumer:
    print(f"Received: {message.value}")
