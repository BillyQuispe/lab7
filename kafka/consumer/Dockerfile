# Usar una imagen de Python ligera
FROM python:3.9-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos de la aplicación
COPY requirements.txt requirements.txt
COPY consumer.py consumer.py

# Instalar las dependencias
RUN pip install -r requirements.txt

# Ejecutar el consumer
CMD ["python", "consumer.py"]
