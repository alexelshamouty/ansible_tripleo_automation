#!/bin/python

import base
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

class NBox(Driver):
    def get_all_hosts(self):
        print("Code to return host list")

    def get_site_hosts(self, site):
        print("Getting host by site")

        