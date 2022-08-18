#!bin/bin/python3

import sys
import socket
from datetime import datetime
from time import sleep

#BANNER
print("╔╦╗┬ ┬┌┐┌┌─┐┬ ┬ ╔═╗┌─┐┌─┐┌┐┌ ")
print(" ║║│ │││││ ┬└┬┘ ╚═╗│  ├─┤│││ ")
print("═╩╝└─┘┘└┘└─┘ ┴  ╚═╝└─┘┴ ┴┘└┘ ")
print("***********************************************")
print("* Twitter : https://twitter.com/CodeWithDungy *")
print("* GitHub : https://github.com/Dungyy          *")
print("***********************************************")  

#Define Target
target = input(f"Enter IP: ")
startPort = int(input("START PORT: "))
endPort = int(input("END PORT: "))
#if len(sys.argv) == 1:
#    target = socket.gethostbyname(sys.argv[1]) #Translate host to IPV4
#else:
#    print("Invalid amount of arguments")   
#    print("SYNTAX: => python3 scan.py <IP>")
 

print( "*" * 30)
print("Scanning target "+target)
print( "-" * 30)
print("Time started: "+str(datetime.now()))
print( "-" * 30)

port = {}
try:
    for port in range(startPort,endPort):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = s.connect_ex((target,port)) #Returns error indicator
#            print("Checking for port {}".format(port))
            if result == 0:
                print("Port {} is open".format(port))
            #    print( "-" * 30)
           # else:
            #    print("Port {} is closed".format(port))
            #    print( "=" * 50)               
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