import importlib
import config

driver = importlib.import_module(config.interface_driver,"interfaces.drivers")

