import importlib
import config

driver = importlib.import_module(config.interface_driver,"interfaces.drivers")

class DCInterface():
    def __init__(self, host, port, username, password, template):
        self.interface = driver.Driver(host, port, username, password, template)

    def initalize(self):
        return self.interface
