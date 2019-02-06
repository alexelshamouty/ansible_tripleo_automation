#!/bin/python

from interfaces.interface import DCInterface
import argparse

oneView = DCInterface().initalize()

oneView.get_all_hosts()

oneView.get_site_hosts("Moon")
