
from tkinter import *
from tkinter import messagebox
from ValidacionesP1 import Validar
import numpy as np


class Principal():
    def __init__(self):
        self.Val = Validar()
        self.ven = Tk()
        self.ven.geometry("350x250")
        self.lista = []


    def validarCaja(self):
        valor = self.dato.get()
        if valor != "":

            #if (self.Val.ValidarLetra(valor)):
            #    messagebox.showinfo("Correcto","Si comienza con Mayusculas")
            #else:
            #    messagebox.showerror("Incorrecto","No comienza con mayusculas")

            # if (self.Val.ValidarNumeros(valor)):
            #     messagebox.showinfo("Correcto","Si es un numero")
            #     self.lbox.insert((self.lbox.size()+1),valor) # Agregar a listbox
            #     self.dato.delete(0,END) # Borra caja de texto
            # else:
            #     messagebox.showerror("Incorrecto","No es un numero")
            #     self.dato.delete(0,END) # Borrar caja de texto

            if (self.Val.ValidarNumeros(valor)):
                if (self.Val.ValidarEntradas(valor)):
                    self.lbox.insert(self.lbox.size()+1, valor)
                    self.dato.delete(0,END)
                else:
                    messagebox.showerror("Error","No son 2 digitos")
                    self.dato.delete(0,END)
            else:
                messagebox.showerror("Error","No son numeros")
                self.dato.delete(0,END)

            #print(f'La cadena tiene {str(self.Val.ValidarEntradas(valor))}')
            self.label.config(text=f'Numero de elementos: {str(self.lbox.size())}')
        else:
            messagebox.showerror("Error", "Caja de texto vacia")

    def eliminarDato(self):
        if self.lbox.size() <= 0:
            messagebox.showerror("Error", "La lista esta vacia")
            return
        if self.modo.get() == 'Pilas':
            self.lbox.delete(self.lbox.size()-1)
            #Ultimo que entra primero que sale
        else:
            #Primero que entra primero que sale
            self.lbox.delete(0)
        self.label.config(text=f'Numero de elementos: {str(self.lbox.size())}')

    def ordenar(self):
        #burbuja
        #seleccion
        self.lista = list(self.lbox.get(0,END))
        self.arreglo = np.array(self.lista)
        # for i in self.arreglo:
        #     print(i)
        p = 0
        for i in range (p,len(self.lista)):
            p = i
            aux = self.lista[i]
            
            for x in range(0,len(self.lista)):
                #print(self.lista[x])
                if aux < self.lista[x]:
                    aux = self.lista[x]
                    p = x
            self.lista[p] = self.lista[0]
            self.lista[0] = aux
            print(f'mayor {aux} - {self.lista[i]}')
        print(self.lista)



    def inicio(self):
        self.dato = Entry(self.ven)
        self.dato.place(x=100,y=10)
        self.modo = StringVar(value="Pilas")
        Radiobutton(self.ven, text="Pilas", variable=self.modo, value="Pilas").place(x=80,y=50)
        Radiobutton(self.ven, text="Colas", variable=self.modo, value="Colas").place(x=130,y=50)
        Button(self.ven, text="Validar",command=self.validarCaja,width=10).place(x=100,y=100)
        Button(self.ven, text="Eliminar",command=self.eliminarDato,width=10).place(x=200,y=100)
        Button(self.ven, text="Ordenar",command=self.ordenar,width=10).place(x=200,y=150)
        self.label = Label(text="Numero")
        self.label.place(x=100,y=130)
        self.lbox = Listbox(self.ven, bg='white', fg='black', activestyle='dotbox', width=10,height=10, font=("Helvetica",9)) #Listbox
        self.lbox.place(x=20,y=80)
        
        self.ven.mainloop()

    

if __name__=='__main__':
    app = Principal()
    app.inicio()