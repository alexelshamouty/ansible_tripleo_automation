#/bin/python
from interfaces.drivers.base import Base
import pprint
from hpOneView.exceptions import HPOneViewException
from hpOneView.oneview_client import OneViewClient

class Driver(Base):
    def __init__(self, host, port, username, password, template):
        #super(Driver, self).__init__(host, port, username, password, template)
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.template = template

        self.config = {
            "ip": self.host,
            "credentials": {
                "userName": self.username,
                "password": self.password
            }
        }
        self.client = OneViewClient(self.config)

    def get_all_server_hardware(self):
        #Here we need to check only interconnects
        all_servers = self.client.server_hardware.get_all()
        return self._get_server_info(all_servers)

    def get_all_server_hardware_by_template(self):
        #Here we need to check only everything
        #We need to check server profile
        #We need to check all interconnections
        all_servers = self.client.server_hardware.get_all()
        return self._get_server_hardware_by_template(all_servers,self.template)


    def _get_server_hardware_by_template(self, servers, template):
        filteredServers = []
        for server in servers:
            serverProfileUri = server['serverProfileUri']
            if(serverProfileUri):
                templateInfo = self.client.server_profiles.get(serverProfileUri)
                serverProfileTemplateUri = templateInfo['serverProfileTemplateUri']
                profileTemplate = self.client.server_profile_templates.get(serverProfileTemplateUri)
                #If this is the profile that we are looking for
                #Get the iloIPV4 address
                # Check the first boot interface and return it's mac address with the ilo
                if(profileTemplate['name'] == template):
                    boot_interface = None
                    iloIPV4 = server['mpHostInfo']['mpIpAddresses'][0]['address']
                    #Get the ilo address
                    #Get the interface mac address
                    for interface in templateInfo['connections']:
                        if (interface['boot']['priority'] == 'Primary'):
                            boot_interface = interface['mac']
                            break
                    filteredServers.append({
                        "mac_address" : boot_interface,
                        "iloIPV4" : iloIPV4
                    })
        return filteredServers

    def _get_server_info(self, servers):
        serversList = []
        for server in servers:
            #Only list servers with profiles
            serverProfileUri = server['serverProfileUri']
            if(serverProfileUri):
                boot_interface = None
                iloIPV4 = server['mpHostInfo']['mpIpAddresses'][0]['address']
                templateInfo = self.client.server_profiles.get(serverProfileUri)
                serverProfileTemplateUri = templateInfo['serverProfileTemplateUri']
                for interface in templateInfo['connections']:
                    if (interface['boot']['priority'] == 'Primary'):
                        boot_interface = interface['mac']
                        break
                serversList.append({
                    "mac_address" : boot_interface,
                    "iloIPV4" : iloIPV4
                })
        return serversList
'''
    def get_all_profiles(self):
        all_profiles = self.client.server_profiles.get_all()
        for profile in all_profiles:
            boot_interface = "none"
            hostname = "none"
            serverHardwareUri = "none"
            iloIPV4 = "none"

            # Get this server information
            boot_interface, hostname, serverHardwareUri, iloIPV4 = self._get_server_info_from_profile(profile)
            # We got the information we need, time to get the ILO IP address

            

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

    def _get_server_info_from_profile(self, profile, template="None"):
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
'''