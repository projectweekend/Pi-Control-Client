from distutils.core import setup

setup(
    name='Pi-Control-Client',
    version='1.0.0',
    author='Brian Hines',
    author_email='brian@projectweekend.net',
    packages=['pi_control_client'],
    url='http://pypi.python.org/pypi/Pi-Control-Client/',
    license='LICENSE.txt',
    description='A client to controlling a Raspberry Pi running Pi-Control-Service (https://github.com/projectweekend/Pi-Control-Service).',
    long_description=open('README.txt').read(),
    install_requires=[
        "pika == 0.9.14",
    ],
)
