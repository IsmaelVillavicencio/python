from tkinter import *
from Cilindro import Cilindro
from tkinter import messagebox as mbox
class App():
    def __init__(self):
        self.root = Tk()
        self.root.config(bd=15)
        self.vx = StringVar()
        self.vy = StringVar()
        self.vr = StringVar()
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
        self.lbl_x = Label(self.root,text="X:")
        self.inp_x = Entry(self.root, textvariable=self.vx)

        self.lbl_y = Label(self.root,text="Y:")
        self.inp_y = Entry(self.root, textvariable=self.vy)

        self.lbl_r = Label(self.root,text="Radio:")
        self.inp_r = Entry(self.root, textvariable=self.vr)

        self.lbl_a = Label(self.root,text="Altura:")
        self.inp_a = Entry(self.root, textvariable=self.va)

        self.btn = Button(self.root, text="Calcular", command=self.show)

        self.lbl_x.grid(column=0, row=0, padx=10, pady=5)
        self.inp_x.grid(column=1, row=0, padx=10, pady=5)

        self.lbl_y.grid(column=0, row=1, padx=10, pady=5)
        self.inp_y.grid(column=1, row=1, padx=10, pady=5)

        self.lbl_r.grid(column=0, row=2, padx=10, pady=5)
        self.inp_r.grid(column=1, row=2, padx=10, pady=5)

        self.lbl_a.grid(column=0, row=3, padx=10, pady=5)
        self.inp_a.grid(column=1, row=3, padx=10, pady=5)
        self.btn.grid(column=1, row=4, padx=10, pady=5)
        self.root.mainloop()

    def show(self):
        x = int(self.inp_x.get())
        y = int(self.inp_y.get())
        r = int(self.inp_r.get())
        a = int(self.inp_a.get())
        Cilindro.__init__(self,x,y,r,a)
        Cilindro.setX(self, x)
        Cilindro.setY(self, y)
        Cilindro.setRadio(self, r)
        Cilindro.setAltura(self, a)
        ifo = " El valor de X es: "+str(Cilindro.getX(self))+"\n El valor de Y es: "+str(Cilindro.getY(self))+"\n El valor del radio es: "+str(Cilindro.getRadio(self))+"\n El valor de la altura es: "+str(Cilindro.getAltura(self))+"\n El valor del volumen es: "+str(Cilindro.getVolumen(self))
        mbox.showinfo("Information", ifo)


def delete(self):
    self.inp_x.set('')
    self.inp_y.set('')
    self.inp_r.set('')
    self.inp_a.set('')

def main():
    app = App()
    return 0

if __name__ == '__main__':
    main()
