import socket
import random
import logging
from threading import *
import threading
N=int(input("height of tree"))
Number_nodes=(2**(N+1))-1
print(Number_nodes)
global Marked_nodes
Marked_nodes=[]

global count
global just
just=0
count=0
thread_running = True

class Node:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data
      self.marked=False
   def PrintTree(self):
      print(self.data)
def build_empty(root,n,i):
    
    if(i>=N):
        return
    else:
        #print(n,i)
        root.left=Node(2*n)
        root.right=Node(2*n+1)
        #print(2*n,2*n+1,"here")
    if(i>=Number_nodes):
        return
    else:
        build_empty(root.left,2*n,i+1)
        build_empty(root.right,2*n+1,i+1)
    
root=Node(1)
ROOT=root
build_empty(root,1,0)
def print_tree(root):
    if(root is not None):
        print(root.data,root.marked,"hrer")
        print_tree(root.left)
        print_tree(root.right)
def is_marked_all(root=ROOT):
   
   if(root is not None):
       #print(root.data,root.marked,"hrer")
      return root.marked*is_marked_all(root.left)*is_marked_all(root.right)
   else:
      return True  
#print_tree(root)
def mark(root,num):
    if(root is not None):
        if(root.data == num):
            
            root.marked=True
            Marked_nodes.append(str(root.data))
            #print("marked",num,root.data,reut.data)
        else:
            mark(root.left,num)
            mark(root.right,num)
def check_child(root):
   #print("started",root.data)
   if(is_marked_all(root)):
      return
   global Marked_nodes
   if(root is not None ):
      #print("OYUTHASKJD")
      try:
         if(root.marked and root.left is not None and root.right.marked and not root.left.marked ):
            root.left.marked=True
            Marked_nodes.append(str(root.left.data))
            print(root.left.data,"in this")
      except:
         pass
      try:
         if(root.marked and root.right is not None and root.left.marked and not root.right.marked ):
            root.right.marked=True
            Marked_nodes.append(str(root.right.data))
            print(root.right.data,"in this right")
      except:
         pass
      check_child(root.left)
      check_child(root.right)
   if(root is not None):
      try:
         if(not root.marked and root.left.marked and root.right.marked):
            root.marked=True
            print(root.data,"in this root")
            Marked_nodes.append(str(root.data))
      except:
         pass
      check_child(root.left)
      check_child(root.right)
   else:
      return 
   #print(c)

#mark(root,3)
#print_tree(root)
def thread_function():
   #print("in herE")
   global just
   just+=1
   global thread_running
   c=0
    # run this while there is no input
   #print(thread_running)
   
      #print("inside thread tunnig")
   try:
      check_child(ROOT)
         #print(reut.data,"reuut")
   except:
      pass
   #print("c",c)
def take_input():
    msgFromServer = UDPClientSocket.recvfrom(bufferSize)
    mark(root,int(msgFromServer[0]))
    import time
    #time.sleep(2)
    # doing something with the input
    print('The user input is: ', msgFromServer)
    
    global count
    count+=1
all_processes=['process1','process2','process3']

msgFromClient       = random.choice(all_processes)

bytesToSend         = str.encode(msgFromClient)


serverAddressPort   = ("127.0.0.1", 20001)

bufferSize          = 1024



# Create a UDP socket at client side

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

UDPClientSocket.sendto(bytesToSend, serverAddressPort)
UDPClientSocket.sendto(bytesToSend, serverAddressPort)
bytesToSend = str.encode(str(Number_nodes))

    #thread_running = True
    #print(bytesToSend)
UDPClientSocket.sendto(bytesToSend, serverAddressPort)

# Send to server using created UDP socket

t1=Thread(target=thread_function,daemon=True)
t1.start();

while(1):
    #print("i",i)
    
    bytesToSend = str.encode(str(is_marked_all()))
    
    if(is_marked_all()):
       UDPClientSocket.sendto(bytesToSend, serverAddressPort)
       #UDPClientSocket.sendto(bytesToSend, serverAddressPort)
       break
    #thread_running = True
    #print(bytesToSend)
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)
    Marked_nodes_all=str.encode(' '.join(Marked_nodes))
    print("markeD",Marked_nodes_all)
    
    UDPClientSocket.sendto(Marked_nodes_all, serverAddressPort)
    
    Marked_nodes=[]
    #msgFromServer = UDPClientSocket.recvfrom(bufferSize)
    #mark(root,int(msgFromServer[0]))
    #msg = "Message from Server {}".format(msgFromServer[0])
    if(not t1.is_alive()):
       #print("here thread")
       t1=Thread(target=thread_function,daemon=True)
       t1.start();
    take_input();
    
    '''t1 = Thread(target=thread_function)
    t2 = Thread(target=take_input)
    e = threading.Event()
    t2.start()
    t1.start()
    
    #t2.join(3)
    #e.set()
    t2.join()  # interpreter will wait until your process get completed or terminated
    thread_running = not thread_running'''
    

    #print(msg)
#print("last")
print(count)
print(just)
