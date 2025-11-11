# Hacer un programa que lea nombre, apellido materno y paterno en 3 cajas separadas, ademas leer dia, mes, y año de nacimiento
# en 3 cajas separadas.
# Al presionar un boton se agregara a un listbox el rfc de la persona, ademas contendra 2 botones para eliminar elementos del listbox
# mediante pilas y colas.

from tkinter import *
from tkinter import messagebox
from ValidacionP2 import Validacion



class Principal():
    def __init__(self):
        self.ven = Tk()
        self.ven.geometry("500x500")
        self.ven.title("Programa 2")
        self.valid = Validacion

    def agregar(self):
        nom = self.entr1.get()
        app = self.entr2.get()
        apm = self.entr3.get()

        dia = self.entr4.get()
        mes = self.entr5.get()
        año = self.entr6.get()

        if self.valid.validarNombre(nom):
            pass

    def eliminar(self):
        pass

    def inicio(self):
        
        Label(self.ven,text="Nombre").place(x=50,y=50)
        self.entr1 = Entry(self.ven)
        self.entr1.place(x=30,y=80)

        Label(self.ven,text="Apellido P.").place(x=220,y=50)
        self.entr2 = Entry(self.ven)
        self.entr2.place(x=200,y=80)

        Label(self.ven,text="Apellido M.").place(x=370,y=50)
        self.entr3 = Entry(self.ven)
        self.entr3.place(x=360,y=80)


        Label(self.ven,text="Dia").place(x=50,y=120)
        self.entr4 = Entry(self.ven)
        self.entr4.place(x=30,y=150)

        Label(self.ven,text="Mes").place(x=220,y=120)
        self.entr5 = Entry(self.ven)
        self.entr5.place(x=200,y=150)

        Label(self.ven,text="Año").place(x=370,y=120)
        self.entr6 = Entry(self.ven)
        self.entr6.place(x=360,y=150)

        self.modo = StringVar(value="Pilas")
        Radiobutton(self.ven, text="Pilas",variable= self.modo,value="Pilas").place(x=50,y=200)
        Radiobutton(self.ven, text="Colas",variable= self.modo,value="Colas").place(x=120,y=200)

        Button(self.ven,text="Eliminar",command=self.eliminar).place(x=220,y=200)
        Button(self.ven,text="Agregar",command=self.agregar).place(x=300,y=200)

        self.lbox = Listbox(self.ven, bg='white', fg='black', activestyle='dotbox', width=15,height=15)
        self.lbox.place(x=200,y=250)


        self.ven.mainloop()





if __name__=='__main__':
    app = Principal()
    app.inicio()