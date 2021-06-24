#! /usr/bin/python3.9

import paramiko
import time
import sys
import traceback

'''
THIS SECTION IS USED AS AN OUTER LOOP AS IT PULLS
IN IP ADDRESSES OR HOST NAMES FROM A FILE NAMED hosts.txt.
'''
def main():
    INPUT_FILE = "hosts.txt"
    f = open(INPUT_FILE, "r")
    all_ips = [x.rstrip() for x in f]
    for line in all_ips:
        ip = line
        open_conn(ip)  #CALLS THE OPERATION 'open_conn'


'''
THIS SECTION IS CALLED BY THE MAIN AND PASSED THE IP ADDRESS OF THE
TARGET HOST. A TELNET CONNECTION IS OPENED AND THE STATIC USER/PASS
COMBINATION IS USED BELOW. EXECUTED COMMANDS ARE STORED IN A FILE CALLED
COMMANDS.TXT. COMMANDS SHOULD FOLLOW STANDARD CISCO SYNTAX
'''

def open_conn(ip):
    try:
        #Define ssh parameters
        username = 'pomi9003'
        password = 'Dnielsen$954'
        port = 22
        timeout = 3
        reading_timeout = 5

        #Logging into device
        connection = paramiko.SSHClient()
        connection.connect(hostname=ip, username=username, password=password)
#        print("connecting to " + ip + "\n")

        stdin,stdout,stderr=conn.exec_command('show run | include 10.7.79.250')
        host_output = stdout.readlines()

        for items in host_output:
            print(items)

if __name__=="__main__":
    try:
        main()
    except:
        print ("Trigger Exception, traceback info forward to log file.")
        traceback.print_exc(file=open("temp.log","w"))

        sys.exit(1)


