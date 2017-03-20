# -*- coding: utf-8 -*-
from Tkinter import * #gives us access to everything in the Tkinter class
import tkMessageBox
from PIL import Image, ImageTk
import random
import time

LUI_encryption = dict()
LUI_decryption = dict()

def encrypt_message(msg):
    e = int(e2.get())
    n = int(e1.get())

    print msg
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
    d = 4637
    n = 11911
    decrypted_msg = ""
    for i in msg: 
        if i in LUI_decryption:
            decrypted_msg += LUI_decryption[i]
        else:
            numberize = ord(i)
            encrypt = pow(numberize, d, n)
            LUI_decryption[i] = unichr(encrypt)
            decrypted_msg += unichr(encrypt)
    return decrypted_msg
    

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
        
def startcodon():
    if  len(e2.get()) or len(e1.get()) == 0:
        tkMessageBox.showinfo("Title", "a Tk MessageBox")
    message = t1.get("1.0", END)
    final_encrypted_message =encrypt_message(message)
    t1.delete("1.0", END)
    t1.insert("1.0", final_encrypted_message)

def endcodon():
    message = t2.get("1.0", END)
    t2.delete("1.0", END)
    t2.insert("1.0", decrypt_message(message))
    
        
 
    
    

root = Tk() #gives us a blank canvas object to work with
root.title = ("GUI Program")

button1 = Button(root, text="Encrypt", command=startcodon)
button1.grid(row=1, column=3)

button2 = Button(root, text="Decrypt", command =endcodon)
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


