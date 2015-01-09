from rpc import RPCClient


class CustomActionClient(RPCClient):

    def __init__(self, rabbit_url, device_key):
        super(CustomActionClient, self).__init__(
            rabbit_url=rabbit_url,
            queue_name='custom_action_service',
            device_key=device_key)

    def call(self, action_name):
        return self._call({'action': action_name})
