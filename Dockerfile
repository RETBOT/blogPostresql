# Obtener imagen base
FROM --platform=linux/amd64 python:3.10.9-slim-buster

# Establecer las variables de entorno 
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Establecer direcorio de trabajo
WORKDIR /code

# Instalar dependencias
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Copiar proyecto
COPY . .