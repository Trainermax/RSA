# -*- coding: utf-8 -*-
from Tkinter import * #gives us access to everything in the Tkinter class
import tkMessageBox
from PIL import Image, ImageTk
import random
import time

e=5
n=11911
d = 4637

LUI_encryption = dict()
LUI_decryption = dict()

def encrypt_message(msg):
    
    encrypted_msg = ""
    for i in msg: 
        if i in LUI_encryption:
            encrypted_msg += LUI_encryption[i]
        else:
            numberize = ord(i)
            encrypt = pow(numberize, e, n)
            LUI_encryption[i] = unichr(encrypt)
            encrypted_msg += unichr(encrypt)
    return encrypted_msg

def decrypt_message(msg):
    decrypted_msg = ""
    for i in msg: 
        if i in LUI_encryption:
            decrypted_msg += LUI_encryption[i]
        else:
            numberize = ord(i)
            encrypt = pow(numberize, d, n)
            LUI_encryption[i] = unichr(encrypt)
            decrypted_msg += unichr(encrypt)
    return decrypted_msg
    
message = "mississippi"
final_encrypted_message =encrypt_message(message)
print final_encrypted_message
print decrypt_message(final_encrypted_message)

def openfileR():
    f = open("Readme.txt", "r")
    for line in f:
        listbox1.insert(END,line)
def openfileW():
    f = open("Readme.txt", 'w')
    names = listbox1.get(0,END)
    for i in names:
        f.write(i + "\n")
        f.close()
        

    
    

root = Tk() #gives us a blank canvas object to work with
root.title = ("GUI Program")

button1 = Button(root, text="Encrypt", command=encrypt_message)
button1.grid(row=1, column=3)

button2 = Button(root, text="Decrypt", command =decrypt_message)
button2.grid(row=1, column = 20)

t1 = Text(root, height=10, width=25)
t1.grid(row=3, column=1)
t2 = Text(root, height=10, width=25)
t2.grid(row=3, column=20)

e1 = Entry(root)
e2 = Entry(root)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)


Label(root, text="n").grid(row=0)
Label(root, text="e").grid(row=1)

 
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=openfileR)
filemenu.add_command(label="Save", command=openfileW)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.destroy)
menubar.add_cascade(label="File", menu=filemenu)

root.config(menu=menubar)


mainloop() #causes the windows to display on the screen until program closes


