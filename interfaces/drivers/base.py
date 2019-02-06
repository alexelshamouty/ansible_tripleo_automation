#!/bin/python

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

class Driver:
    def __init__(self, host, port, use_ssl=False, auth_token='token'):
        self.port = port
        self.host = host
        self.use_ssl = use_ssl
        self.auth_token = auth_token

    def get_all_hosts(self):
        pass

    def get_site_hosts(self, site):
        pass

        