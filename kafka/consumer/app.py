from kafka import KafkaConsumer
from flask import Flask, jsonify
import json
import threading

app = Flask(__name__)
music_data_list = []

# Configuración del consumidor
consumer = KafkaConsumer(
    'music_topic',
    bootstrap_servers='kafka:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='music_group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

def consume_messages():
    global music_data_list
    for message in consumer:
        music_data_list.append(message.value)
        print(f"Received: {message.value}")

@app.route('/api/music', methods=['GET'])
def get_music():
    return jsonify(music_data_list)

if __name__ == '__main__':
    # Inicia el hilo para consumir mensajes
    threading.Thread(target=consume_messages, daemon=True).start()
    app.run(host='0.0.0.0', port=5002)
