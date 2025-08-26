#Imagen para correr python
FROM python:3.9-slim

# Evitar que Python guarde .pyc y mejorar logs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Crear directorio de la app dentro del contenedor
WORKDIR /app

# Instalar dependencias del sistema (ejemplo: para psycopg2, numpy, etc.)
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copiar dependencias del proyecto
COPY requirements.txt .

# Instalar dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código del proyecto
COPY . .

# Puerto expuesto (modifica según tu app)
EXPOSE 8000

# Comando para correr la aplicación
CMD ["python", "main.py"]