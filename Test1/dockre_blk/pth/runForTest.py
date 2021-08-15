import sys
import os
os.system('sudo apt install python3-six&&sudo pip3 install ansible junos-eznc jxmlease ncclient&&ansible-galaxy install Juniper.junos')
from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from jnpr.junos.exception import ConnectError

def junSend(host_name,user_name,passw_name,command):
    try:
        dev = Device(host=host_name, user=user_name, password=passw_name)
        dev.open()
        dev.timeout = 300
    except ConnectError as err:
        print ("Cannot connect to device: {0}".format(err))
        return
    with Config(dev, mode='private') as cu:  
        #cu.load('set firewall filter F-EGRESS term DENY-ATTACKERS from source-address '+ ipAddr, format='set')
        cu.load(command, format='set')
        if cu.diff():
            cu.commit()
        cu.commit()
    dev.close()
junSend("1.1.1.1","user_name","passw_name","command")
