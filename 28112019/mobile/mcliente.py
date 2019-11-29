from tkinter import *
from tkinter import messagebox as mbox
import socket
import sys

class App():
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect the socket to the port where the server is listening
    server_address = ('192.168.43.14', 10000)
    print('connecting to {} port {}'.format(*server_address))
    sock.connect(server_address)

    def __init__(self):
        self.root = Tk()
        self.root.config(bd=15)
        self.va = StringVar()
        # Gets the requested values of the height and widht.
        windowWidth = self.root.winfo_reqwidth()
        windowHeight = self.root.winfo_reqheight()
        #print("Width",windowWidth,"Height",windowHeight)
        # Gets both half the screen width/height and window width/height
        positionRight = int(self.root.winfo_screenwidth()/2 - windowWidth/2)
        positionDown = int(self.root.winfo_screenheight()/2 - windowHeight/2)

        # Positions the window in the center of the page.
        self.root.geometry("+{}+{}".format(positionRight, positionDown))
        self.root.resizable(width=False,height=False)
        self.root.title('Título')

        self.lbl_a = Label(self.root,text="Valor:")
        self.inp_a = Entry(self.root, textvariable=self.va)

        self.btn = Button(self.root, text="Calcular", command=self.show)

        self.lbl_a.grid(column=0, row=3, padx=10, pady=5)
        self.inp_a.grid(column=1, row=3, padx=10, pady=5)
        self.btn.grid(column=1, row=4, padx=10, pady=5)
        self.root.mainloop()

    def show(self):
        x = str(self.inp_a.get())
        try:

            # Send data
            message = x
            #print('sending {!r}'.format(message))
            self.sock.send(message.encode())

            # Look for the response
            print(message)
            amount_received = 0
            amount_expected = len(message)
            cont = 0
            while amount_received < 15:
                data = self.sock.recv(16)
                valor = int(str(data.decode()))
                amount_received +=1
                valor = valor + 1
                self.sock.send(str(valor).encode())
                print('datos',valor)
                #print('received {!r}'.format(data.decode()))

        finally:
            print('closing socket')
            self.sock.close()

def main():
    app = App()
    return 0

if __name__ == '__main__':
    main()
