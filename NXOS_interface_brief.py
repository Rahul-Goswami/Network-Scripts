from netmiko import ConnectHandler

# Create a dictionary for Cisco Device

cisco_device = {
    'device_type': 'cisco_nxos',
    'ip': '10.1.1.10',
    'username': '',
    'password': '',
    'port': '',
    'secret': '',
    'verbose': True
}

# Create a connection to the Cisco Device
print('Connecting to' + cisco_device['ip'])
conn = ConnectHandler(**cisco_device)

#Create logic for commands
output = conn.send_command('show ip interface brief')
print(type(output))
print(output)

#Close connection
print("Disconnecting from device")
conn.disconnect()


