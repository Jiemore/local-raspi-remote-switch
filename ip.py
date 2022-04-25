import ifcfg
import json
import time

def getInterface():
    device = {
        'device':{},
        'time':time.strftime('%Y-%m-%d %H:%M:%S'),
        'name':'rp'
        }

    for name, interface in ifcfg.interfaces().items():
        # do something with interface
        device['device'][interface['device']] = interface['inet'] 
        #print interface['inet4']        # List of ips
        #print interface['inet6']
        #print interface['netmask']
        #print interface['broadcast']

    return json.dumps(device)

#default = ifcfg.default_interface()
