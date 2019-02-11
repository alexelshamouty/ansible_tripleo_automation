#!/bin/python
import argparse

def cli():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--host", help="IP/Domain name of the Data Center inventory", 
                    required=True)
    parser.add_argument("--port", help="Port to use to connect to the Data Center inventory", 
                    default=443, nargs='?')
    parser.add_argument("--username", help="Username to connect to the Data Center inventory", 
                    required=True)
    parser.add_argument("--password", help="Password to connect to the Data Center inventory", 
                    required=True)
    parser.add_argument("--template", help="Password to connect to the Data Center inventory", 
                    default="None", nargs='?')
    parser.add_argument("--debug", help="Print debugging information", default="no", 
                        nargs="?", 
                        choices=["yes","no"])
    arguments = parser.parse_args()
    return arguments

            