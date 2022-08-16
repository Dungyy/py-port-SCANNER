#!bin/bin/python3

import sys
import socket 
from datetime import datetime

#Define Target
target = input(f"IP: ")

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) #Translate host to IPV4
else:
    print("Invalid amount of arguments")   
    print("SYNTAX: => python3 scan.py <IP>")

#BANNER

print( "=" * 50)
print("Scanning target "+target)
print( "-" * 50)
print("Time started: "+str(datetime.now()))
print( "=" * 50)

try:
    for port in range(1,85):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = s.connect_ex((target,port)) #Returns error indicator
            if result == 0:
                print("Port {} is open".format(port))
            s.close()

except KeyboardInterrupt:
    print("\nExiting Program")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved.")
    sys.exit()

except socket.error:
    print("couldn't connect to server")
    sys.exit()