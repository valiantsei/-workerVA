import sys
import os
from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from jnpr.junos.exception import ConnectError

import threading
import signal

def checkAddrMask(ipMask):
    if "/" in ipMask and len(ipMask.split("/")) and ipMask.split("/")[1].isdigit():
            if int(ipMask.split("/")[1])>=0 and int(ipMask.split("/")[1])<33:
                if "." in ipMask and len(ipMask.split("."))==4:
                    ipDigit = ipMask.split("/")[0].split(".")
                    for xTmp in ipDigit:
                        if not xTmp.isdigit():
                            return False
                        if int(xTmp) < 0 or int(xTmp) > 255:
                            return False
                    return True
    return False
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
	
hostList=['1.1.1.1','2.2.2.2','3.3.3.3']
userList=['a1','a2','a3']
passList=['b1','b2','b3']

def threadWorks():
    if os.path.exists('/usr/share/ipADD'):
        addrList = {}
        with open('/usr/share/ipTmp','a+') as f:
            f.seek(0,0)
            addrList = f.read().splitlines()
            f.truncate(0)
    
        for ipAddr in addrList:
            if checkAddrMask(ipAddr):
                commandTmp = 'command for add ip to blk '+ ipAddr
                for i in range(hostList):
                    junSend(hostList[i],userList[i],passList[i],commandTmp)
                with open('/usr/share/tmp','w') as f:
                    f.write(ipAddr)

    if os.path.exists('/usr/share/ipDEL'):
        addrList = {}
        with open('/usr/share/ipTmp','a+') as f:
            f.seek(0,0)
            addrList = f.read().splitlines()
            f.truncate(0)
    
        for ipAddr in addrList:
            if checkAddrMask(ipAddr):
                commandTmp = 'command for del ip in list blk '+ ipAddr
                for i in range(hostList):
                    junSend(hostList[i],userList[i],passList[i],commandTmp)

                with open('/usr/share/tmp','w') as f:
                    f.write(ipAddr)
       
    #change time to 1800.0
    timer = threading.Timer(180.0, threadWorks)
    timer.start()

threadWorks()
