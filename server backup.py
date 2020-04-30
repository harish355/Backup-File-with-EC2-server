import socket
import os
import time
import threading


s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', Port))
while(1):
   s.listen(10)
   csock,address=s.accept()
   
