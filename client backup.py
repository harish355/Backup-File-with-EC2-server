import socket
import os
import time
from tkinter import *
import Tkinter, Tkconstants, tkFileDialog

def backup():
    # Enter Backup
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c.connect(("ip address", 1234))

    FileName = raw_input("Enter Filename to download from server : ")
    Data = "Temp"

    while True:
        c.send(FileName)
        Data = c.recv(1024)
        DownloadFile = open(FileName, "wb")
        while Data:
            DownloadFile.write(sData)
            Data = skClient.recv(1024)
        print("Download Completed")
        break

    skClient.close()

root = Tk()
root.filename = tkFileDialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
print (root.filename)

