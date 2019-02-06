#!/bin/python

from interfaces.drivers.base import Base

try:
    import requests
except ImportError:
    sys.exit('requestst package is required')

#This code should not care at all about anything related to ansible 
#Nor should it care at all about anything related to another tool
#This code will return the current values ONLY
#IPMIusername:
#IPMIPassword
#Macaddress
#Profile of the compute node ( compute / controller )

#Only filteration that is allowed is site filteration
#We request information based on the site 

class Driver(Base):
    def initialize():
        super(OneView, self).__init__(host, port)

    def get_all_hosts(self):
        print("Code to return host list from %s:%s " % ( self.host, self.port ) )

    def get_site_hosts(self, site):
        print("Getting host by site")
        