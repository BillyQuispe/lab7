# Usar la imagen oficial de PostgreSQL desde Docker Hub
FROM postgres:15-alpine

# Exponer el puerto predeterminado de PostgreSQL
EXPOSE 5432

# Copiar el script de inicialización si lo tienes
COPY init.sql /docker-entrypoint-initdb.d/

# Comando para iniciar el servidor PostgreSQL
CMD ["postgres"]
