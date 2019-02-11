#!/bin/python

#This code should not care at all about anything related to ansible 
#Nor should it care at all about anything related to another tool
#This code will return the current values ONLY
#IPMIusername:
#IPMIPassword
#Macaddress
#Profile of the compute node ( compute / controller )

#Only filteration that is allowed is site filteration
#We request information based on the site 

class Base:
    def __init__(self, host, port, username, password, template, use_ssl=False, auth_token='token'):
        self.port = port
        self.host = host
        self.username = username
        self.password = password
        self.use_ssl = use_ssl
        self.auth_token = auth_token
    
    def initialize(self, host, port):
        pass

    def get_all_profiles(self):
        pass
        
    def get_all_hosts(self):
        pass

    def get_site_hosts(self, site):
        pass

        