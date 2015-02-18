from rpc import RPCClient


class CustomActionClient(RPCClient):

    def __init__(self, rabbit_url):
        super(CustomActionClient, self).__init__(
            rabbit_url=rabbit_url,
            exchange='custom_action_control')

    def call(self, device_key, action_name):
        return self._call(device_key, {'action': action_name})
