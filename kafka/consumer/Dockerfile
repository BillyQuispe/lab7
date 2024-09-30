# Usar una imagen base de Python
FROM python:3.9-slim

# Crear y establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar los archivos de dependencias y el código a la imagen
COPY requirements.txt requirements.txt
COPY app.py app.py

# Instalar las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto 5002 para Flask
EXPOSE 5002

# Comando para ejecutar la aplicación Flask
CMD ["python", "app.py"]
