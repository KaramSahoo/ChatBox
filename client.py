import socket
from tkinter import *

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip=socket.gethostbyname(socket.gethostname())

s.connect((ip,80))

root = Tk()
root.title("Client")

messages = Text(root)
input_user = StringVar()
input_field = Entry(root,text=input_user)
input_field.pack(side=BOTTOM, fill=X)

def EnterPressed(event):
	input_get = input_field.get()
	messages.insert(INSERT, 'Sent : %s\n'%input_get)
	s.send(bytes(input_get, encoding='utf-8'))
	input_user.set('')
	messages.insert(INSERT, 'Received : %s\n'%s.recv(1024).decode('utf-8'))
	input_user.set('')

messages.pack()
input_field.bind("<Return>", EnterPressed)

root.mainloop()
