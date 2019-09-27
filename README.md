# Cisco_Telnet

This simple script should be used to execute a variety of commands against multiple devices, using telnet remote access.
The script is written to run in Python 2.7 and should not be run in Python 3.x

## Getting Started

The script and the feed-files must all be located in the same directory. The script reads the file named "hosts.txt",
which should include hostnames or IP addresses of all target devices. The file named "commands.txt" should contain one
or more configuration commands to be executed on the devices defined in the "hosts.txt" file.

### Prerequisites

- The following modules are required to run the script: telnetlib, time, sys, and traceback.
- The hosts.txt file must contain IP addresses or hostnames of devices to target
- Telnet access is required on target devices
- commands.txt file must contain configuration commands. Show commands will fail

### Installing

1. Install Python 2.7 with full standard libraries
2. Download files from https://github.com/mikepowe/Cisco_Telnet and place all files in the same directory

    For Example:

    $ pwd
    /Users/mikepowell/Documents/GitHub/Cisco_Telnet

    $ ls -l
    total 40
    -rw-r--r--  1 mikepowell  staff  2522 Sep 27 14:10 README.md
    -rw-r--r--  1 mikepowell  staff    94 Sep 26 16:25 commands.txt
    -rw-r--r--  1 mikepowell  staff    27 Sep 26 16:25 hosts.txt
    -rw-r--r--  1 mikepowell  staff  3311 Sep 26 16:25 telnet_with_input_loop.py
    -rw-r--r--  1 mikepowell  staff   695 Sep 26 16:25 temp.log

I can see all files are located in my directory.
3. Ensure commands.txt and hosts.txt have read privileges for any user


## Running the tests

1. Open command prompt and CD to folder containing script and files.
2. Update hosts.txt file to  include target hosts. This is what the host file looks like initially
     $ cat hosts.txt
     10.196.8.57
     1.1.1.1
     2.2.2.2

and these entries should be replaced with your specific target devices. Hostnames will also work if DNS can resolve the
names.

3. Update the commands.txt file with whatever commands you will apply to the target devices. Config mode is entered
 before the file is called, so "config t" is not needed.

     Example of command.txt:
     $ cat commands.txt
     username CISCO password CISCO
     username NETOPS password CISCO123
     snmp-server community CISCO RO

 These commands should be replaced with your specific commands



Now, to run the script, run the following and wait:

    $ python telnet_with_input_loop.py
    10.196.8.57 passed
    1.1.1.1 failed
    2.2.2.2 failed

You can see that the first device passed and configs were applied, but the other 2 failed to complete. There is no
detailed reporting of error types. Typically, the script fails due to incorrect username/password, or unreachable device.

