import json
import pika
import uuid


class RPCClient(object):

    def __init__(self, rabbit_url, exchange):
        self._rabbit_url = rabbit_url
        self._exchange = exchange
        self._connection = pika.BlockingConnection(pika.URLParameters(self._rabbit_url))
        self._setup_channel()

    def _setup_channel(self):
        self._channel = self._connection.channel()

        result = self._channel.queue_declare(exclusive=True)
        self._rpc_response_queue = result.method.queue

        self._channel.basic_consume(
            self._handle_rpc_response,
            no_ack=True,
            queue=self._rpc_response_queue)

    def _handle_rpc_response(self, ch, method, props, body):
        if self._correlation_id == props.correlation_id:
            self._rpc_response = body

    def _call(self, routing_key, message):
        self._rpc_response = None
        self._correlation_id = str(uuid.uuid4())
        self._channel.basic_publish(
            exchange=self._exchange,
            routing_key=routing_key,
            properties=pika.BasicProperties(
                reply_to=self._rpc_response_queue,
                correlation_id=self._correlation_id),
            body=json.dumps(message))

        while self._rpc_response is None:
            self._connection.process_data_events()

        return json.loads(self._rpc_response)
