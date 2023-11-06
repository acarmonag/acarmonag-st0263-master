from concurrent import futures
import grpc
import Service_pb2
import Service_pb2_grpc
import os
import datetime
from config import*


# Implementación del servicio ProductService
class ProductService(Service_pb2_grpc.ProductServiceServicer):
   
   # Implementación de la función SearchProduct
   def SearchProduct(self, request, context):
      print("Solicitud recibida para buscar producto: " + request.busqueda)
      
      # Buscar el archivo en el directorio
      for archivo in os.listdir(RUTA_ARCHIVOS):
         archivo_respuesta = []
         if request.busqueda in archivo:
            ruta_archivo = os.path.join(RUTA_ARCHIVOS, archivo)
            fecha_modificacion = datetime.datetime.fromtimestamp(os.path.getmtime(ruta_archivo)).strftime('%Y-%m-%d %H:%M:%S')
            tamaño = os.path.getsize(ruta_archivo) / (1024*1024) # Tamaño en MB
            archivo_respuesta.append(Service_pb2.singleTransactionResponse(nombre=archivo, last_updated=fecha_modificacion, size=tamaño))
            yield Service_pb2.multipleTransactionResponse(files=archivo_respuesta)
            

   # Implementación de la función ListProducts
   def ListProducts(self, request, context):
      print("Solicitud recibida para listar productos")
      
      archivos_respuesta = []
      for archivo in os.listdir(RUTA_ARCHIVOS):
         ruta_archivo = os.path.join(RUTA_ARCHIVOS, archivo)
         fecha_modificacion = datetime.datetime.fromtimestamp(os.path.getmtime(ruta_archivo)).strftime('%Y-%m-%d %H:%M:%S')
         tamaño = os.path.getsize(ruta_archivo) / (1024 * 1024) # Tamaño en MB
         archivos_respuesta.append(Service_pb2.singleTransactionResponse(nombre=archivo, last_updated=fecha_modificacion, size=tamaño))
      
      yield Service_pb2.multipleTransactionResponse(files=archivos_respuesta)

def serve():
    # Crear el servidor gRPC
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    Service_pb2_grpc.add_ProductServiceServicer_to_server(ProductService(), server)
    server.add_insecure_port(HOST)
    print("El servicio está corriendo en", HOST)
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()