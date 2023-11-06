# https://medium.com/better-programming/introduction-to-message-queue-with-rabbitmq-python-639e397cb668
# consumer.py
# Consume RabbitMQ queue

import json
import pika
import glob
import os
import datetime
from dotenv import load_dotenv
from config import*

load_dotenv()

HOST_RABBITMQ = os.getenv('HOST_RABBITMQ')
PORT_RABBITMQ = os.getenv('PORT_RABBITMQ')
USER_RABBITMQ = os.getenv('USER_RABBITMQ')
PASSWORD_RABBITMQ = os.getenv('PASSWORD_RABBITMQ')

print("El servicio está corriendo en Servidor2")

connection = pika.BlockingConnection(pika.ConnectionParameters(HOST_RABBITMQ, PORT_RABBITMQ, '/', pika.PlainCredentials(USER_RABBITMQ, PASSWORD_RABBITMQ)))
channel = connection.channel()

def SearchProduct(ch, method, properties, body):
    requestbusqueda = body.decode('utf-8')
    print("Solicitud recibida para buscar producto: " + requestbusqueda)
      
    archivo_respuesta = []
    for archivo in os.listdir(RUTA_ARCHIVOS):
         if requestbusqueda in archivo:
            ruta_archivo = os.path.join(RUTA_ARCHIVOS, archivo)
            fecha_modificacion = datetime.datetime.fromtimestamp(os.path.getmtime(ruta_archivo)).strftime('%Y-%m-%d %H:%M:%S')
            tamaño = os.path.getsize(ruta_archivo) / (1024*1024) # Tamaño en MB
            archivo_respuesta.append({"nombre":archivo, "last_updated":fecha_modificacion, "size":tamaño})

    publish_response(ch, method, properties, archivo_respuesta)

def ListProducts(ch, method, properties, body):
    print("Solicitud recibida para listar productos por rabbitmq")
      
    archivos_respuesta = []
    for archivo in os.listdir(RUTA_ARCHIVOS):
        ruta_archivo = os.path.join(RUTA_ARCHIVOS, archivo)
        fecha_modificacion = datetime.datetime.fromtimestamp(os.path.getmtime(ruta_archivo)).strftime('%Y-%m-%d %H:%M:%S')
        tamaño = os.path.getsize(ruta_archivo) / (1024 * 1024) # Tamaño en MB
        archivos_respuesta.append({"nombre":archivo, "last_updated":fecha_modificacion, "size":tamaño})

    publish_response(ch, method, properties, archivos_respuesta)

def publish_response(ch, method, properties, response):
    
    channel.basic_publish(
        exchange='',
        routing_key=properties.reply_to,
        properties=pika.BasicProperties(
            correlation_id=properties.correlation_id,
        ),
        body=json.dumps(response)
    )
    ch.basic_ack(delivery_tag=method.delivery_tag)
    print("Respuesta de rabbitmq enviada")
    
channel.basic_consume(queue="q1", on_message_callback=ListProducts, auto_ack=False)
channel.basic_consume(queue="q2", on_message_callback=SearchProduct, auto_ack=False)
channel.start_consuming()