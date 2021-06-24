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
        #Define telnet parameters
        username = 'pomi9003'
        password = 'Dnielsen$954'
        port = 22
        timeout = 3
        reading_timeout = 5

        #Logging into device
        connection = paramiko.SSHClient()
        connection.connect(ip, username=username, password=password)
#        print("connecting to " + ip + "\n")

        #Waiting for the username prompt and sending the username
        output = connection.read_until("Username:", reading_timeout)
        connection.write(username + "\n")
        time.sleep(2)

        #Waiting for the password prompt and sending the password
        output = connection.read_until("Password:", reading_timeout)
        connection.write(password + "\n")
        time.sleep(2)


        #Setting terminal length for entire output - no pagination
        connection.write("terminal length 0\n")
        time.sleep(1)


        #Enter Enable Mode (Priv lvl 15)
        connection.write("enable\n")
        time.sleep(2)

        #Waiting for the password prompt and sending the password
        output = connection.read_until("Password:", reading_timeout)
        connection.write(password + "\n")
        time.sleep(2)

        #Entering global config mode
        connection.write("\n")
        connection.write("configure terminal\n")
        time.sleep(2)

        #Open user selected file for reading
        selected_cmd_file = open("commands.txt", "r")

        #Starting from the beginning of the file
        selected_cmd_file.seek(0)

        #Writing each line in the file to the device
        for each_line in selected_cmd_file.readlines():
            connection.write(each_line + '\n')
            time.sleep(2)

        connection.write("end\n")
        connection.write("write memory\n")
        connection.write("exit\n")
        time.sleep(2)

        #Closing the file
        selected_cmd_file.close()

        #Write output to log file
        # str_all = connection.read_all()
        # log = open("log_out.txt", 'a')
        # log.write(str_all)


        #Test for reading command output
     #   switch_output = connection.read_very_eager()
     #   print switch_output

        #Closing the connection and logging success
        connection.close()
        print(ip + " passed")


    #Logging Exception Failure
    except IOError:
        print(ip + " failed")


if __name__=="__main__":
    try:
        main()
    except:
        print ("Trigger Exception, traceback info forward to log file.")
        traceback.print_exc(file=open("temp.log","w"))

        sys.exit(1)


