import grpc
import Service_pb2 as Service_pb2
import Service_pb2_grpc as Service_pb2_grpc
from dotenv import load_dotenv
import os

load_dotenv()

GRPC_HOST= os.getenv('GRPC_HOST')

class RecursosGRPC:
    def __init__(self, host= GRPC_HOST):
        # Crear un canal de comunicación con el servidor gRPC
        self.canal = grpc.insecure_channel(host)
        # Crear un cliente para el servicio ProductService
        self.cliente = Service_pb2_grpc.ProductServiceStub(self.canal)

    def buscar_producto(self, nombre_archivo):
        respuestas = []
        for respuesta_stream in self.cliente.SearchProduct(Service_pb2.Archive(busqueda=nombre_archivo)):
            for archivo in respuesta_stream.files:
                respuestas.append({"nombre": archivo.nombre, "last_updated": archivo.last_updated, "size": archivo.size})
        return respuestas

    def listar_productos(self):
        archivos = []
        for respuesta_stream in self.cliente.ListProducts(Service_pb2.Empty()):
            for archivo in respuesta_stream.files:
                archivos.append({"nombre": archivo.nombre, "last_updated": archivo.last_updated, "size": archivo.size})
        return archivos
