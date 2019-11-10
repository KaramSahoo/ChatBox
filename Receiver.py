import socket
from tkinter import *

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip=socket.gethostbyname(socket.gethostname())

s.bind((ip,80))
s.listen()

client,addr=s.accept()

root = Tk()
root.title("Receiver")

input_user = StringVar()
input_field = Entry(root,text=input_user)
input_field.pack(side=BOTTOM, fill=X)

messages = Text(root)

def receive():
	messages.insert(INSERT, 'Received : %s\n'%client.recv(1024).decode('utf-8'))

def EnterPressed(event):
	input_get = input_field.get()
	messages.insert(INSERT, 'Sent : %s\n'%input_get)
	client.send(bytes(input_get, encoding='utf-8'))
	input_user.set('')


messages.pack()
button = Button(root, text="display message", command=receive).pack()
input_field.bind("<Return>", EnterPressed)
root.mainloop()
