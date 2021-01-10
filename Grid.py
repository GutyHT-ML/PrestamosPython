from tkinter import *
from Prestamo import Prestamo as p
from Material import Material as m
class GridView(Frame):
    Prestamos = []
    def __init__(self, master):
        Frame.__init__(self, master)
        self.init_frame()
    def init_frame(self):
        self.pack(fill=BOTH, expand=1)
        column_1 = Label(self, text="Usuario")
        column_1.grid(row=0, column=0)
        column_2 = Label(self, text="Materiales")
        column_2.grid(row=0, column=1)
        column_3 = Label(self, text="Fecha")
        column_3.grid(row=0, column=2)
        list_1 = Listbox(self)
        list_1.grid(row=1,column=0)
        for x in range(len(self.Prestamos)):
            list_1.insert(x, self.Prestamos[x].Beneficiado)
        list_2 = Listbox(self)
        list_2.grid(row=1,column=1)
        for x in range(len(self.Prestamos)):
            Str = ""
            for y in self.Prestamos[x].Materiales:
                Str+=y+", "
            list_2.insert(x ,Str)
        list_3 = Listbox(self)
        list_3.grid(row=1,column=2)
        for x in range(len(self.Prestamos)):
            list_3.insert(x, self.Prestamos[x].Fecha)
    def grid_update(self, lend):
        self.Prestamos.append(lend)
        self.init_frame()

