from socket import *

def showall(u, addr, st,k):
  n=0
  str=''
  while(n<k):
    str = str + u[n] + ' ' + st[n] + '\n'
    n = n + 1
  print(str)
  #print("Hello from a function")
  return str

def showallServer(u, addr, st,k):
  n=0
  str=''
  while(n<k):
    str=str + u[n]+' '+st[n]+'\n'
    n=n+1
  print(str)
  #print("End offunction")

def searchUser(userID, u,addr ,k, ms,ca,messageo):
  n=0
  ms = ms.decode()
  ms = ms.split()
  messageo = messageo.decode()
  while(n<k):
    if u[n]==userID:
      del ms[0]
      del ms[0]
      j=0
      while (j<k):
        if addr[j]== ca:
          messageo = messageo+ ' , from '+ users[j]
        j=j+1
      #ms.append(', '+)
      messageo = messageo.encode()
      address = addr[n]
      serverSocket.sendto(messageo, address)
      print("message sent")
      return True
    n=n+1
  return False

def sendToAll(u,adrr,k,ms):
  n=0
  while(n<k):
    address = adrr[n]
    serverSocket.sendto(ms, address)
    n=n+1
  print("message send to all users")
serverSocket = socket(AF_INET, SOCK_DGRAM)  #Server Socket Object created
serverSocket.bind(('',12000))               #Bind Created
print('The server is ready to receive')     #Server will receive messages from clients
i=0
users = []
ipadress =[]
status= []
while True:                                 #Entering the loop STATE_1
  try:
    message,clientAddress = serverSocket.recvfrom(1024) #Socket receives message from client STATE_2
  except:
    print("lost connection")
  msg= message.decode()
  msg= msg.split()
  #if message.decode() == 'logging':
  if msg[0] == 'logging':
    users.append(msg[1])
    ipadress.append(clientAddress)
    status.append('active')
    i=i+1
    print(msg[1]+' has logging')
    message=msg[1]+' has logging'
    message = message.encode()
    showallServer(users,ipadress,status, i)
    sendToAll(users,ipadress,i,message)

  elif msg[0] == 'showall' or msg[0]=='SHOWALL':
    message=showall(users,ipadress,status, i)
    message= message.encode()
    serverSocket.sendto(message, clientAddress)
  elif msg[0] == 'logout':
    print('user has logout')
    #sendToAll(users, ipadress, i, message)
    j = 0
    while (j < i):
      if ipadress[j] == clientAddress:
        name= users[j]
        status[j] = 'inactive'
      j = j + 1
    message= name+' has logged out\n'
    message=message.encode()
    sendToAll(users, ipadress, i, message)
  elif len(msg)>2 and searchUser(msg[0],users,ipadress,i,message,clientAddress,message)==True:
      message = 'message sent'
      message = message.encode()
      serverSocket.sendto(message, clientAddress)
  else:
    print("user not found")
 # message='Hello'
  #message= message.encode()
 # serverSocket.sendto(message, clientAddress)         #Socket sends response message to client STATE_3
