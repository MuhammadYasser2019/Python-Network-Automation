
#import connecthandler for ssh and datetime for exection time calculation
from netmiko import ConnectHandler
from datetime import datetime

#for parsing out to json
import json


#list of targeted routers 
routerRight = {
        'device_type': 'cisco_ios',
        'host':'192.168.85.20',
        'username':'yasser',
        'password':'12345',
}
routerLeft = {
        'device_type': 'cisco_ios',
        'host':'192.168.85.21',
        'username':'foad',
        'password':'12345',
}
routerDown = {
        'device_type': 'cisco_ios',
        'host':'40.40.40.10',
        'username':'yahia',
        'password':'12345',
}

#putting targted routers in list for looping
allDevices=[routerRight,routerLeft,routerDown]


start_time = datetime.now()
for device in allDevices:

    connection = ConnectHandler(**device)
    connection.enable()
     
    #targeted output 
    rmodel = connection.send_command("show version | in revision")
    hostname = connection.send_command("show run | in hostname")
    uptime = connection.send_command("show version | in uptime")
    sversion = connection.send_command("show version | in Version")
    hwSerial = connection.send_command("show Inventory | in Hw")
    # mac = connection.send_command("show interfaces | in Gi.*up|bia")
    mac = connection.send_command("show ip arp | in -",use_textfsm=True)

    #putting output in Dic for parsing
    device = {
        'HOSTNAME  ': hostname,
        'MODEL  ': rmodel,
        'UPTIME  ': uptime,
        'SOFTWARE  ': sversion,
        'SERIAL NUMBER  ': hwSerial,
        'MAC ADDRESS  ' : mac,

    }

    end_time = datetime.now() 
    total_time = end_time - start_time 
    
    #parsing output Dic to json
    out=json.dumps(device, indent=1)
    print("------------------------------- Output-------------------------------")
    print(out)
print("------------------------------- Execution Time--------------------------------")
print(total_time) 
print("------------------------------------- End --------------------------------------")