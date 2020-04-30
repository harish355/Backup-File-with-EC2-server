import sys
import socket
import os
workingdir = "/root/backup/"
host = ''
port=1234
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
print("Server Active")

while(1):
   s.listen(10)
   FileFound = 0
   while True:
       c, Address = s.accept()
       print Address
       FileName = c.recv(1024)
       for file in os.listdir(workingdir):
           if file == FileName:
               FileFound = 1
               break
       if(FileFound == 0):
           print(FileName + " Not Found On Server")
       else:
           print(FileName + " File Found")
           fUploadFile = open("files/" + FileName, "rb")
           Read = UploadFile.read(1024)
           while Read:
               c.send(Read)
               Read = UploadFile.read(1024)
           print "Sending Completed"
       break
   c.close()
   s.close()

