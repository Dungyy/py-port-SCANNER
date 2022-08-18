from time import sleep
import socket, ipaddress, threading

print(r'''
                                                  
@@@@@@@   @@@  @@@  @@@  @@@   @@@@@@@@  @@@ @@@  
@@@@@@@@  @@@  @@@  @@@@ @@@  @@@@@@@@@  @@@ @@@  
@@!  @@@  @@!  @@@  @@!@!@@@  !@@        @@! !@@  
!@!  @!@  !@!  @!@  !@!!@!@!  !@!        !@! @!!  
@!@  !@!  @!@  !@!  @!@ !!@!  !@! @!@!@   !@!@!   
!@!  !!!  !@!  !!!  !@!  !!!  !!! !!@!!    @!!!   
!!:  !!!  !!:  !!!  !!:  !!!  :!!   !!:    !!:    
:!:  !:!  :!:  !:!  :!:  !:!  :!:   !::    :!:    
 :::: ::  ::::: ::   ::   ::   ::: ::::     ::    
:: :  :    : :  :   ::    :    :: :: :      :     
 @@@@@@    @@@@@@@   @@@@@@   @@@  @@@            
@@@@@@@   @@@@@@@@  @@@@@@@@  @@@@ @@@            
!@@       !@@       @@!  @@@  @@!@!@@@            
!@!       !@!       !@!  @!@  !@!!@!@!            
!!@@!!    !@!       @!@!@!@!  @!@ !!@!            
 !!@!!!   !!!       !!!@!!!!  !@!  !!!            
     !:!  :!!       !!:  !!!  !!:  !!!            
    !:!   :!:       :!:  !:!  :!:  !:!            
:::: ::    ::: :::  ::   :::   ::   ::            
:: : :     :: :: :   :   : :  ::    :             
                                                  
''')

ip = input(f"Enter Local IP: ")
port = {}
max_threads = 50
#final = {}
startPort = int(input("START PORT: "))
endPort = int(input("END PORT: "))
def check_port(ip, port):
    for port in range(startPort, endPort + 1):
        try:
            tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            if not tcp.connect_ex((ip, port)):
                print("\n")
                print(ip + " is Connected")
            else:
                result == 0
            # print ("Port is open")
            print('[+] %s:%d | TCP Open' % (ip, port))    
            tcp.close()
        except Exception:
            pass


for ip in ipaddress.IPv4Network(ip):
    threading.Thread(target=check_port, args=[str(ip), port]).start()
    #sleep(0.1)

    # limit the number of threads.
    while threading.active_count() > max_threads :
        sleep(1)


print("\n*************************************************")
print("\n* Twitter : https://twitter.com/CodeWithDungy   *")
print("\n* GitHub : https://github.com/Dungyy            *")
print("\n*************************************************")
print ("")
#print(final)
