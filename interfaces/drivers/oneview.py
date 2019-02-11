#/bin/python
from interfaces.drivers.base import Base
from hpOneView.exceptions import HPOneViewException
from hpOneView.oneview_client import OneViewClient

class Driver(Base):
    def __init__(self, host, port, username, password):
        super(Driver, self).__init__(host, port, username, password)
        self.config = {
            "ip": self.host,
            "credentials": {
                "userName": self.username,
                "password": self.password
            }
        }
        self.client = OneViewClient(self.config)

    def get_all_hosts(self):
        all_profiles = self.client.server_profiles.get_all()
        for profile in all_profiles:
            print(' %s' % profile['name'])

    def get_site_hosts(self, site):
        print("Getting host by site(%s) from %s:%s " % (site, self.host, self.port ) )