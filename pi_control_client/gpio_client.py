from rpc import RPCClient


class GPIOClient(RPCClient):

    def __init__(self, rabbit_url, device_key):
        super(GPIOClient, self).__init__(
            rabbit_url=rabbit_url,
            queue_name='gpio_service',
            device_key=device_key)

    def on(self, pin_number):
        return self._call({'pin': pin_number, 'action': 'on'})

    def off(self, pin_number):
        return self._call({'pin': pin_number, 'action': 'off'})

    def read(self, pin_number):
        return self._call({'pin': pin_number, 'action': 'read'})

    def get_config(self, pin_number=None):
        if pin_number:
            return self._call({'pin': pin_number, 'action': 'get_config'})
        return self._call({'action': 'get_config'})
