This is a client library for remotely controlling a Raspberry Pi that is running [Pi-Control-Service](https://github.com/projectweekend/Pi-Control-Service). After following the instructions for setting up the service, you will need to reuse the same RabbitMQ connection string and device key values to start a client.


## Install it

```
pip install Pi-Control-Client
```

## GPIO client

The GPIO client (`pi_control_client.GPIOClient`) is used to control a Raspberry Pi running the GPIO service. More information about the service can be found [here](https://github.com/projectweekend/Pi-Control-Service) in the **GPIO service** section.


### Using the GPIO client

```python
from pi_control_client import GPIOClient

# The RabbitMQ connection string (must match the one used when starting the service)
RABBIT_URL='some_actual_connection_string'

# A unique string you make up to identify a single Raspberry Pi (must match the one used when starting the service)
DEVICE_KEY='my_awesome_raspberry_pi'

pins_client = GPIOClient(rabbit_url=RABBIT_URL, device_key=DEVICE_KEY)

# Get all pins config
result = pins_client.get_config()

# Get a pin config
result = pins_client.get_config(18)

# Turn a pin on
pins_client.on(18)

# Turn a pin off
pins_client.off(18)

# Read a pin value
result = pins_client.read(18)
```


## Custom action client

The custom action service (`pi_control_service.CustomActionService`) is used to control a Raspberry Pi running the custom action service. More information about the service can be found [here](https://github.com/projectweekend/Pi-Control-Service) in the **Custom action service** section.


### Using the custom action client

```python
from pi_control_client import CustomActionClient

# The RabbitMQ connection string (must match the one used when starting the service)
RABBIT_URL='some_actual_connection_string'

# A unique string you make up to identify a single Raspberry Pi (must match the one used when starting the service)
DEVICE_KEY='my_awesome_raspberry_pi'

actions_client = CustomActionClient(rabbit_url=RABBIT_URL, device_key=DEVICE_KEY)

# Call a custom action
result = actions_client.call('name_of_action_method')
```
