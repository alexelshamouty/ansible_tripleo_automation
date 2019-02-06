#!/bin/python
from ansible.plugins.inventory import BaseInventoryPlugin
from interfaces.interface import DCInterface
import argparse

def cli():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--list", help="Print all hosts in Json for ansible")
    parser.add_argument("--host", help="Print specefic host vars in Json for ansible")
    arguments = parser.parse_args()
    return arguments

class InventoryModule(BaseInventoryPlugin):
    NAME = 'tripleOinventory'

if __name__ == "main":
    cli()
