#!/bin/python

try:
    import requests
except ImportError:
    sys.exit('requestst package is required')

class Driver:
    def __init__(self, host, port, use_ssl=False, auth_token='token'):
        self.port = port
        self.host = host
        self.use_ssl = use_ssl
        self.auth_token = auth_token

    def initalize(self):
        print("I am returing!")
        