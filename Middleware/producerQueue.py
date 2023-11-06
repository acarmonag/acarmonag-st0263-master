import json 
import pika 
from dotenv import load_dotenv
import os
import uuid

load_dotenv()
HOST_RABBITMQ = os.getenv('HOST_RABBITMQ')
PORT_RABBITMQ = os.getenv('PORT_RABBITMQ')
USER_RABBITMQ = os.getenv('USER_RABBITMQ')
PASSWORD_RABBITMQ = os.getenv('PASSWORD_RABBITMQ')
EXCHANGE_RABBITMQ = os.getenv('EXCHANGE_RABBITMQ')

class AMQPRpcClient(object):
    def __init__(self):
        self.connection=pika.BlockingConnection(
            pika.ConnectionParameters(
                host=HOST_RABBITMQ, 
                port=PORT_RABBITMQ, 
                credentials=pika.PlainCredentials(USER_RABBITMQ, PASSWORD_RABBITMQ)
                )
            )
        self.channel=self.connection.channel()
        result=self.channel.queue_declare(queue='', exclusive=True)
        self.callback_queue=result.method.queue
        
        self.channel.basic_consume(
            queue=self.callback_queue,
            on_message_callback=self.on_response,
            auto_ack=True
            )
        self.response=None
        self.corr_id=None
        self.function=None
    
    def on_response(self, ch, method, props, body):
        if self.corr_id==props.correlation_id:
            self.response=body
        
    def call(self, body):
        self.response=None
        self.corr_id= str(uuid.uuid4())
        self.channel.basic_publish(
            exchange=EXCHANGE_RABBITMQ,
            routing_key=self.function,
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id
                ),
            body=body)
        self.connection.process_data_events(time_limit=None)
        return self.response
    
def RunAMQP(body, function=""):
    amqp_rpc_client=AMQPRpcClient()
    amqp_rpc_client.function=function
    response=amqp_rpc_client.call(body)
    return json.loads(response.decode('utf-8'))
            
            