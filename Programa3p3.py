from tkinter import *
from tkinter import messagebox
from ValidacionesP1 import Validar
import numpy as np

class Principal():
    def __init__(self):
        self.val = Validar()
        self.ven = Tk()
        self.lis=[]
        self.ven.title('Programa 3')
        ancho = 350
        alto = 250
        pantalla_ancho = self.ven.winfo_screenmmwidth()
        pantalla_alto = self.ven.winfo_screenmmheight()
        x = (pantalla_alto//2)- (ancho//2)
        y = (pantalla_ancho//2)- (alto//2)
        self.ven.geometry(f"{ancho}x{alto}+{x+350}+{y-350}")

    def quitar_placeholder(self, event):
        if self.dato.get() == self.placeholder:
            self.dato.delete(0, END)
            self.dato.config(fg="black")

    def poner_placeholder(self, event):
        if self.dato.get() == self.placeholder:
            self.dato.insert(0, self.placeholder)
            self.dato.config(fg="gray")

    def inicio(self):
        self.placeholder = "Nombre"
        self.dato = Entry(self.ven, fg="gray")
        self.dato.insert(0, self.placeholder)
        self.dato.bind("<FocusIn>", self.quitar_placeholder)





if __name__=='__main__':
    app = Principal()
    app.inicio()