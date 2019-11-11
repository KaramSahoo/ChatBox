import socket
from tkinter import *
from threading import Thread

def menu():
	root = Tk()
	root.title("Menu")
	root.geometry("100x100")

	client_btn = Button(text="Client",command=client)
	receiver_btn = Button(text="Receiver",command=receiver)
	client_btn.pack()
	receiver_btn.pack()

	root.mainloop()

def client():

	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	ip=socket.gethostbyname(socket.gethostname())

	s.connect((ip,80))

	root = Tk()
	root.title("Client")
	root.geometry("200x200")

	messages = Text(root)
	input_user = StringVar()
	input_field = Entry(root,text=input_user)
	input_field.pack(side=BOTTOM, fill=X)

	def EnterPressed(event):
		input_get = input_field.get()
		messages.insert(INSERT, 'Sent : %s\n'%input_get)
		s.send(bytes(input_get, encoding='utf-8'))
		input_user.delete(0, 'end')

	messages.pack()

	def Receive():
		while True:
			recv_msg = s.recv(1024).decode('utf-8')
			messages.insert(INSERT, 'Received : %s\n' % recv_msg)
			input_user.delete(0, 'end')

	def Send():
		while True:
			input_field.bind("<Return>", EnterPressed)

	Thread(target=Send).start()
	Thread(target=Receive).start()

	root.mainloop()

def receiver():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	ip = socket.gethostbyname(socket.gethostname())

	s.bind((ip, 80))
	s.listen()

	client, addr = s.accept()

	root = Tk()
	root.title("Receiver")
	root.geometry("200x200")

	input_user = StringVar()
	input_field = Entry(root, text=input_user)
	input_field.pack(side=BOTTOM, fill=X)

	def EnterPressed(event):
		input_get = input_field.get()
		messages.insert(INSERT, 'Sent : %s\n' % input_get)
		client.send(bytes(input_get, encoding='utf-8'))
		input_user.delete(0, 'end')

	messages = Text(root)
	messages.pack()
	messages.insert(INSERT, str(addr) + " Connected\n")
	input_field.bind("<Return>", EnterPressed)

	def Receive():
		while True:
			recv_msg = client.recv(1024).decode('utf-8')
			messages.insert(INSERT, 'Received : %s\n' % recv_msg)

	def Send():
		while True:
			input_field.bind("<Return>", EnterPressed)

	Thread(target=Send).start()
	Thread(target=Receive).start()
	root.mainloop()

if __name__ == "__main__":
	menu()
