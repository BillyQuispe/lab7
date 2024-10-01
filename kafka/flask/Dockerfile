# Usar una imagen de Python ligera
FROM python:3.9-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos de la aplicación
COPY requirements.txt requirements.txt
COPY app.py app.py

# Instalar las dependencias
RUN pip install -r requirements.txt

# Ejecutar la aplicación Flask
CMD ["python", "app.py"]
