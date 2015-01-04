import json
import pika
import uuid


class RPCClient(object):

    def __init__(self, rabbit_url, queue_name, device_key):
        self.rabbit_url = rabbit_url
        self.queue_name = queue_name
        self.device_key = device_key
        self.connection = pika.BlockingConnection(pika.URLParameters(self.rabbit_url))
        self._setup_channel()

    def _setup_channel(self):
        self.channel = self.connection.channel()
        self.channel.exchange_declare(exchange=self.device_key, type='direct')

        result = self.channel.queue_declare(exclusive=True)
        self.rpc_response_queue = result.method.queue

        self.channel.basic_consume(
            self._handle_rpc_response,
            no_ack=True,
            queue=self.rpc_response_queue)

    def _handle_rpc_response(self, ch, method, props, body):
        if self.correlation_id == props.correlation_id:
            self.rpc_response = body

    def _call(self, message):
        self.rpc_response = None
        self.correlation_id = str(uuid.uuid4())
        self.channel.basic_publish(
            exchange=self.device_key,
            routing_key=self.queue_name,
            properties=pika.BasicProperties(
                reply_to=self.rpc_response_queue,
                correlation_id=self.correlation_id),
            body=json.dumps(message))

        while self.rpc_response is None:
            self.connection.process_data_events()

        return json.loads(self.rpc_response)
