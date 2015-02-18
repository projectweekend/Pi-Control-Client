from rpc import RPCClient


class GPIOClient(RPCClient):

    def __init__(self, rabbit_url):
        super(GPIOClient, self).__init__(
            rabbit_url=rabbit_url,
            exchange='gpio_control')

    def on(self, device_key, pin_number):
        return self._call(device_key, {'pin': pin_number, 'action': 'on'})

    def off(self, device_key, pin_number):
        return self._call(device_key, {'pin': pin_number, 'action': 'off'})

    def read_value(self, device_key, pin_number):
        return self._call(device_key, {'pin': pin_number, 'action': 'read'})

    def read_config(self, device_key, pin_number=None):
        if pin_number:
            return self._call(device_key, {'pin': pin_number, 'action': 'get_config'})
        return self._call(device_key, {'action': 'get_config'})
