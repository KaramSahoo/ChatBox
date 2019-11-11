import socket
from tkinter import *
from threading import Thread

menu_window = Tk()


def menu():
    menu_window.title("Menu")
    menu_window.geometry("180x80")
    Label(text="Choose Receiver or Client").place(x=17, y=5)
    client_btn = Button(menu_window, text="Client", command=client)
    receiver_btn = Button(menu_window, text="Receiver", command=receiver)
    client_btn.place(x=30, y=30)
    receiver_btn.place(x=90, y=30)
    menu_window.mainloop()


def client():
    menu_window.destroy()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ip = socket.gethostbyname(socket.gethostname())

    s.connect((ip, 80))

    root = Tk()
    root.title("Client")
    root.geometry("200x200")

    messages = Text(root)
    input_user = StringVar()
    input_field = Entry(root, text=input_user)
    input_field.pack(side=BOTTOM, fill=X)

    def EnterPressed(event):
        input_get = input_field.get()
        messages.insert(INSERT, 'Sent : %s\n' % input_get)
        s.send(bytes(input_get, encoding='utf-8'))

    messages.pack()

    def Receive():
        while True:
            recv_msg = s.recv(1024).decode('utf-8')
            messages.insert(INSERT, 'Received : %s\n' % recv_msg)

    def Send():
        while True:
            input_field.bind("<Return>", EnterPressed)

    Thread(target=Send).start()
    Thread(target=Receive).start()

    root.mainloop()


def receiver():
    menu_window.destroy()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ip = socket.gethostbyname(socket.gethostname())

    s.bind((ip, 80))
    s.listen()

    root = Tk()
    root.title("Receiver")
    root.geometry("200x200")

    client, addr = s.accept()

    input_user = StringVar()
    input_field = Entry(root, text=input_user)
    input_field.pack(side=BOTTOM, fill=X)

    def EnterPressed(event):
        input_get = input_field.get()
        messages.insert(INSERT, 'Sent : %s\n' % input_get)
        client.send(bytes(input_get, encoding='utf-8'))

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
