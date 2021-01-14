from tkinter import *
from Prestamo import Prestamo
from Material import Material
class GridView(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.init_frame()
    def init_frame(self):
        self.pack(fill=BOTH, expand=1)
        label_beneficiado = Label(self, text="Usuario")
        label_beneficiado.grid(row=0, column=0)
        label_materiales = Label(self, text="Materiales")
        label_materiales.grid(row=0, column=1)
        label_fecha = Label(self, text="Fecha")
        label_fecha.grid(row=0, column=2)
        list_beneficiado = Listbox(self)
        list_beneficiado.grid(row=1,column=0)
        list_materiales = Listbox(self)
        list_materiales.grid(row=1,column=1)
        list_fecha = Listbox(self)
        list_fecha.grid(row=1,column=2)
        for x in Prestamos:
            list_beneficiado.insert(END, x.beneficiado.nombre)
            Str = ""
            mats = ""
            for y in x.materiales:
                mats += Str + y.nombre + ", "
            list_materiales.insert(END , mats)
            list_fecha.insert(END, x.fecha)
    def grid_update(self, lend):
        Prestamos.append(lend)
        self.init_frame()
Prestamos = []


