#import socket
from socket import *
import sys

id = sys.argv[1]        #takes a parameter in command prompt

clientSocket = socket(AF_INET, SOCK_DGRAM) #creates a socket  STATE_1
msg = 'logging '+id
clientSocket.sendto(msg.encode(), ('172.30.80.244',12000))
t='pass'                      # assign pass to t so user enters to loop

while t!='exit':              # entering loop, to send messages
  msg, addr = clientSocket.recvfrom(1024)  # arrival of message    STATE_3
  print(msg.decode())  # prints message received (ECHO)
  mgsspl = msg.decode()
  mgsspl = mgsspl.split()
  if len(mgsspl)==3:
    if mgsspl[2]=='logging' and  mgsspl[0]!=id:
      msg, addr = clientSocket.recvfrom(1024)  # arrival of message    STATE_3
      print(msg.decode())  # prints message received (ECHO)

  print("\n to write a message use CLIENT_ID : (message_body)")
  print("\n to see how many users are active write SHOWALL")
  print("\n type update to update the interface\n")
  msg = input('client ' + id + '>')  # dispays the input from the client
  if msg=='exit':                     #verifies if msg = exit
    msg = 'logout'                    #sets msg = logout
    clientSocket.sendto(msg.encode(), ('172.30.80.244', 12000))  #sends logout to SERVER
    t='exit'                          # change t to exit

  else:
    clientSocket.sendto(msg.encode(), ('172.30.80.244',12000)) # message send to a server STATE_2
clientSocket.close()                             #close the socket