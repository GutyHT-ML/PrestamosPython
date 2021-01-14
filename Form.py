from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from typing import Iterable
from Persona import Persona
from Material import Material
from Prestamo import Prestamo as pp
from Grid import GridView as gv
p = Persona("Juan", "Gallardo")
a = Persona("Pedro", "Ramirez")
materials = [Material("Balon"), Material("Red"), Material("Corneta")]
root = Tk()
gridview = gv(root)
class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()
    def init_window(self):
        def save_lend():
            mats = []
            person = Persona.ver_persona(lista_persona.get())
            for x in lista_materiales.curselection():
                mats.append(Material(lista_materiales.get(x)))
            lend = pp(person, fecha_entry.get(), mats)
            gridview.grid_update(lend)
            self.init_window()
        self.master.title("Prestamos")
        self.pack(fill=BOTH, expand=1)
        label_persona = Label(self, text="Usuario")
        label_persona.grid(row=0,column=0)
        lista_persona = ttk.Combobox(self, state="readonly")
        lista_persona.grid(row=0, column=1)
        values = []
        for x in Persona.ver_personas():
            values.append(x.nombre)
        lista_persona["values"] = values
        label_materiales = Label(self, text="Materiales")
        label_materiales.grid(row=1,column=0)
        lista_materiales = Listbox(self, selectmode=MULTIPLE)
        for x in range(len(materials)):
            lista_materiales.insert(x, materials[x].nombre)
        lista_materiales.grid(row=1,column=1)
        label_fecha = Label(self, text="Fecha")
        label_fecha.grid(row=2, column=0)
        fecha_entry = Entry(self)
        fecha_entry.grid(row=2, column=1)
        boton_agregar = Button(self, text="Agregar prestamo", 
        command = save_lend)
        boton_agregar.grid(row=3, column=0, columnspan=2)
app = Window(root)
root.mainloop()