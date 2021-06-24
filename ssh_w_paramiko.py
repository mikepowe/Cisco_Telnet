#!/usr/bin/python3.9

import paramiko

username = "developer"
password = "C1sco12345"

conn = paramiko.SSHClient()
conn.set_missing_host_key_policy(paramiko.AutoAddPolicy)
conn.connect(hostname='ios-xe-mgmt.cisco.com', username=username, password=password, port=8181)

stdin,stdout,stderr=conn.exec_command('show version')

output = stdout.readlines()

for items in output:
    print(items)