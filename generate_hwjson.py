#!/bin/python

from interfaces.interface import DCInterface
from common.cli import cli

arguments = cli()

if (arguments.debug == "yes"):
    print("DEBUG: Connecting to %s:%s with username %s and password %s" %
            (
                arguments.host,
                arguments.port,
                arguments.username,
                arguments.password
            )
        )

oneView = DCInterface(arguments.host,
                        arguments.port,
                        arguments.username,
                        arguments.password).initalize()


oneView.get_all_profiles()
