import importlib
import config

driver = importlib.import_module(config.interface_driver,"interfaces.drivers")

class DCInterface():
    def __init__(self):
        self.interface = driver.Driver(host="127.0.0.1",port="8080")

    def initalize(self):
        return self.interface
