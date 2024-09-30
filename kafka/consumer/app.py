from flask import Flask, jsonify
from kafka import KafkaConsumer
import json

app = Flask(__name__)

# Configurar el consumidor de Kafka
consumer = KafkaConsumer(
    'music_topic',
    bootstrap_servers='kafka:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='music_group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

@app.route('/music', methods=['GET'])
def get_music():
    music_list = []
    for message in consumer:
        music_list.append(message.value)
        if len(music_list) >= 10:  # Recoge los primeros 10 mensajes
            break
    return jsonify(music_list)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)  # Flask corriendo en el puerto 5002
