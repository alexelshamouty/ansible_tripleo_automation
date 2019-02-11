#/bin/python
from interfaces.drivers.base import Base
import pprint
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

    def get_all_profiles(self):
        all_profiles = self.client.server_profiles.get_all()
        for profile in all_profiles:
            boot_interface = "none"
            hostname = "none"
            serverHardwareUri = "none"
            iloIPV4 = "none"

            # Get this server information
            boot_interface, hostname, serverHardwareUri, iloIPV4 = self._get_server_info(profile)
            # We got the information we need, time to get the ILO IP address

            #pp = pprint.PrettyPrinter(indent=4)
            #pp.pprint(profile)
            '''
            print("Following server profile has been found: "
                    "Name: %s "
                    "Mac of PXE: %s "
                    "ServerHardwareUri = %s "
                    "ILO IPV4 = %s " %
                    (
                        hostname,
                        boot_interface,
                        serverHardwareUri,
                        iloIPV4
                    )
                )
            '''
    def get_servers_from_template(self, template):
        pass
    
    def _get_server_info(self, profile, template="None"):
        for interface in profile['connections']:
            if (interface['boot']['priority'] == 'Primary'):
                boot_interface = interface['mac']
                hostname = profile['description']
                serverHardwareUri = profile['serverHardwareUri']
                print("Getting information for this server uri %s " % serverHardwareUri )
                serverHardwareInfo = self.client.server_hardware.get(serverHardwareUri)
                iloIPV4 = serverHardwareInfo['mpHostInfo']['mpIpAddresses'][0]['address']
                #Return all the information in one hit
                print("Following server profile has been found: "
                        "Name: %s "
                        "Mac of PXE: %s "
                        "ServerHardwareUri = %s "
                        "ILO IPV4 = %s " %
                        (
                            hostname,
                            boot_interface,
                            serverHardwareUri,
                            iloIPV4
                        )
                    )
                return boot_interface, hostname, serverHardwareUri, iloIPV4

    def get_all_servers(self):
        pass
    def get_site_hosts(self, site):
        print("Getting host by site(%s) from %s:%s " % (site, self.host, self.port ) )