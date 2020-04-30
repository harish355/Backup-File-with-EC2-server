import socket
import os
import time
from tkinter import *
import Tkinter, Tkconstants, tkFileDialog

def backup():
    # Enter Backup
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c.connect(("Ip Address", port))
    print("Connected to server")

root = Tk()
root.filename = tkFileDialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
print (root.filename)

