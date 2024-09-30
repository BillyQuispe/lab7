from kafka import KafkaConsumer
from flask import Flask, jsonify
from flask_cors import CORS
import json
import threading

app = Flask(__name__)
CORS(app)  # Habilitar CORS para la aplicación

music_data_list = []

# Configuración del consumidor
consumer = KafkaConsumer(
    'music_topic',
    bootstrap_servers='ec2-98-82-15-48.compute-1.amazonaws.com:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='music_group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

def consume_messages():
    global music_data_list
    for message in consumer:
        # Suponiendo que el mensaje recibido es un diccionario con las claves 'a' y 't'
        formatted_message = {
            "a": message.value.get("artist"),  # Cambia 'artist' por la clave correcta en tu JSON
            "t": message.value.get("title")    # Cambia 'title' por la clave correcta en tu JSON
        }
        music_data_list.append(formatted_message)  # Añade el mensaje formateado a la lista
        print(f"Consuming messages from producer: {formatted_message}")  # Indica que está consumiendo un mensaje
        print(f"Current music data list: {music_data_list}")  # Muestra la lista actual de datos de música

@app.route('/api/music', methods=['GET'])
def get_music():
    return jsonify(music_data_list)  # Devuelve la lista de música en formato JSON

if __name__ == '__main__':
    # Inicia el hilo para consumir mensajes
    threading.Thread(target=consume_messages, daemon=True).start()
    
    # Ejecuta la aplicación Flask
    app.run(host='0.0.0.0', port=5002)
