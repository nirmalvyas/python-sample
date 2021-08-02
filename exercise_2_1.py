##script in python for
## TELNET to the server
##Check the disk usage
###inode usage
##get the list of files from the path
##copy file from remote to server using FTP,SFTP and SCP

import getpass
import sys
import telnetlib
import os

def telnet_to_server(host_name, port_no = 80):
    """
    Telnet to the server
    """
    HOST =  host_name
    user = raw("Enter your remote account: ")

    password = getpass.getpass()

    tn = telnetlib.Telnet(HOST)

    tn.read_until("login: ")

    tn.write(user + " ")

    if password:
        tn.read_until("Password: ")
        tn.write(password + " ")

    tn.write("ls")

    tn.write("exit")

    print(tn.read_all())



def disk_usage():
    """
    THis function is used for disk usage
    """
    try:
        cmd = "df"
        os.system(cmd)
    except Exception as e:
        print("Exception in getting disk usage",str(e))