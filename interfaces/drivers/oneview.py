#/bin/python
from interfaces.drivers.base import Base

class Driver(Base):

    def initialize():
        super(OneView, self).__init__(host, port)

    def get_all_hosts(self):
        print("Code to return host list from %s:%s " % ( self.host, self.port ) )

    def get_site_hosts(self, site):
        print("Getting host by site(%s) from %s:%s " % (site, self.host, self.port ) )