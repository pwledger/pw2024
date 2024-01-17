import time
# pure-python-adb loading 
from ppadb.client import Client as AdbClient

def connect():
    client = AdbClient(host="127.0.0.1", port=5037) # Default is "127.0.0.1" and 5037
    devices = client.devices()


    if len(devices) == 0:
        print('No devices')
        quit()

    device = devices[0]
    print(f'Connected to {device}')
    return device, client

connect()