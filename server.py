import socket

 

localIP     = "127.0.0.1"

localPort   = 20001

bufferSize  = 1024
import random
import time
global send_count
send_count=0

msgFromServer       = str(random.randrange(10, 20))

bytesToSend         = str.encode(msgFromServer)

from datetime import datetime



# Create a datagram socket

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

 

# Bind to address and ip

UDPServerSocket.bind((localIP, localPort))

 

print("UDP server up and listening")

 

# Listen for incoming datagrams



bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

message = bytesAddressPair[0]

address = bytesAddressPair[1]
bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
clientMsg = "Message from Client:{}".format(message)
clientIP  = "Client IP Address:{}".format(address)
    
print(clientMsg)
print(clientIP)
bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

message = bytesAddressPair[0]
print("mine",message.decode('utf8'))
N=message.decode('utf8')
All_nums=list(range(1,int(N)+1))
#All_nums=list(range(2,10))
clientMsg='process1'
#All_nums.extend(All_nums)
if('process1' in clientMsg):
    while(1):
        
        send_count+=1
        try:
            bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
        except:
            break

        message = bytesAddressPair[0]


        clientMsg = "Message from Client2:{}".format(message)
        print(clientMsg)
        
        #bytesAddressPair2 = UDPServerSocket.recvfrom(bufferSize)
        #print(message.decode('utf8'))
        if(message.decode('utf8') == '1'):
            #print("naskjdha")
            print(send_count-1)
            break
        try:
            bytesAddressPair2 = UDPServerSocket.recvfrom(bufferSize)
        except:
            break

        message2 = bytesAddressPair[0]


        Marked_nodes_all = (message2.decode('utf8')).split()
        

    
        now = datetime.now()

        current_time = now.strftime("%H:%M:%S")
       # print("Current Time =", current_time)
        now = datetime.now()

        current_time = now.strftime("%H:%M:%S")
        #print("Current Time =", current_time)
        #time.sleep(1)
        msgFromServer       = str(random.choice(All_nums))

        bytesToSend         = str.encode(msgFromServer)

        #All_nums.remove(int(msgFromServer))
        UDPServerSocket.sendto(bytesToSend, address)
    print("here")
elif('process2' in clientMsg):
    while(1):
        
        send_count+=1
        try:
            bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
        except:
            break

        message = bytesAddressPair[0]


        clientMsg = "Message from Client2:{}".format(message)
        print(clientMsg)
        if(message.decode('utf8')=='1'):
            print(send_count-1)
            break
        bytesAddressPair2 = UDPServerSocket.recvfrom(bufferSize)

        message2 = bytesAddressPair[0]


        Marked_nodes_all = (message2.decode('utf8')).split()
        
    
        now = datetime.now()

        current_time = now.strftime("%H:%M:%S")
        #print("Current Time =", current_time)
       # time.sleep(1)
        now = datetime.now()

        current_time = now.strftime("%H:%M:%S")
        #print("Current Time =", current_time)
        try:
            msgFromServer       = str(random.choice(All_nums))
        except:
            break

        bytesToSend         = str.encode(msgFromServer)
        All_nums.remove(int(msgFromServer))
        UDPServerSocket.sendto(bytesToSend, address)
    print("here2")
else:
    while(1):
       
        send_count+=1
        try:
            bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
        except:
            break
        message = bytesAddressPair[0]
        clientMsg = "Message from Client2:{}".format(message)
        print(clientMsg)
        if(message.decode('utf8')== '1'):
            print(send_count-1)
            break 
        bytesAddressPair2 = UDPServerSocket.recvfrom(bufferSize)
        #print(bytesAddressPair2)
        message2 = bytesAddressPair2[0]
        
        Marked_nodes_all = (message2.decode('utf8')).split()
        #print("marked",Marked_nodes_all)
        now = datetime.now()

        current_time = now.strftime("%H:%M:%S")
        #print("Current Time =", current_time)
        #time.sleep(1)
        now = datetime.now()

        current_time = now.strftime("%H:%M:%S")
        #print("Current Time =", current_time)
        #print(Marked_nodes_all)
        All_nums=[x for x in All_nums if(str(x) not in Marked_nodes_all)]
        #print(All_nums)
        msgFromServer       = str(random.choice(All_nums))
        
        bytesToSend         = str.encode(msgFromServer)

        #All_nums.remove(int(msgFromServer))
        UDPServerSocket.sendto(bytesToSend, address)
    print("here3")

