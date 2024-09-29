# Usa una imagen base de Python
FROM python:3.9

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos necesarios al contenedor
COPY producer.py .
COPY music_data.json .

# Instala las dependencias
RUN pip install kafka-python

# Comando por defecto para ejecutar el productor
CMD ["python", "producer.py"]