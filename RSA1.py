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
        if i in LUI_encryption:
            decrypted_msg += LUI_encryption[i]
        else:
            numberize = ord(i)
            encrypt = pow(numberize, d, n)
            LUI_encryption[i] = unichr(encrypt)
            decrypted_msg += unichr(encrypt)
    return decrypted_msg    


def openfileR():
    f = open("Readme.txt", "r")
    for line in f:
        t1.delete("1.0", END)
        t1.insert("1.0", line)
def openfileW():
    f = open("Readme.txt", 'w')
    f.write(t1.get("1.0", END))
    f.close()
   
def startcodon():
    if len(t1.get()) == 0:
        tkMessageBox.showinfo("Error","No input in text")
    message = t1.get("1.0", END)
    final_encrypted_message =encrypt_message(message)
    t1.delete("1.0", END)
    t1.insert("1.0", final_encrypted_message)

def endcodon():
    message = t2.get("1.0", END)
    t2.delete("1.0", END)
    t2.insert("1.0", decrypt_message(message))
    
def directions():
    tkMessageBox.showinfo("Directions","Hello. The N value is derived from multiplying two prime numbers, withthe e value being any prime number that is not divisible by either of the two prime numbers or greater than the n value The set is (n , e) for public keys. Plug in n, e, thentype text into the textbox and hit Encrypt to see the message that is constructed using that public key")
 
    
    

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

filemenu1 = Menu(menubar, tearoff=0)
filemenu1.add_command(label="Open", command=directions)
menubar.add_cascade(label="Directions", menu=filemenu1)

root.config(menu=menubar)




mainloop() #causes the windows to display on the screen until program closes


