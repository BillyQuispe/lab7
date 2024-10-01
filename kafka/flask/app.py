from flask import Flask, jsonify
from kafka import KafkaConsumer
import threading
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 

# Almacena los datos consumidos
dashboard_data = []

consumer = KafkaConsumer(
    'realtime-analytics',
    bootstrap_servers='ec2-98-81-255-236.compute-1.amazonaws.com:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

def kafka_consumer():
    global dashboard_data
    for message in consumer:
        dashboard_data.append(message.value)
        if len(dashboard_data) > 10:  # Mantén los últimos 10 datos
            dashboard_data.pop(0)

threading.Thread(target=kafka_consumer).start()

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(dashboard_data)

@app.route('/')
def index():
    return "Real-time Analytics Dashboard"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
