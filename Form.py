from tkinter import *
from tkinter import messagebox
from Persona import Persona as p
from Material import Material as m
from Prestamo import Prestamo as pp
from Grid import GridView as gv
#import Persona as p
#import Material as m
materials = [m("Balon"), m("Red"), m("Corneta")]
root = Tk()
gridview = gv(root)
class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()
    def init_window(self):
        def save_lend():
            #messagebox.showinfo("ay", "ay")
            mats = []
            for x in listaMateriales.curselection():
                mats.append(listaMateriales.get(x))
            lend = pp(nombrePersona.get(), fechaEntry.get(), mats)
            gridview.grid_update(lend)
            self.init_window()
        self.master.title("Prestamos")
        self.pack(fill=BOTH, expand=1)
        labelPersona = Label(self, text="Usuario")
        labelPersona.grid(row=0,column=0)
        nombrePersona = Entry(self)
        nombrePersona.grid(row=0,column=1)
        labelMateriales = Label(self, text="Materiales")
        labelMateriales.grid(row=1,column=0)
        listaMateriales = Listbox(self, selectmode=MULTIPLE)
        for x in range(len(materials)):
            listaMateriales.insert(x, materials[x].Nombre)
        listaMateriales.grid(row=1,column=1)
        labelFecha = Label(self, text="Fecha")
        labelFecha.grid(row=2, column=0)
        fechaEntry = Entry(self)
        fechaEntry.grid(row=2, column=1)
        botonAgregar = Button(self, text="Agregar prestamo", 
        command = save_lend)
        botonAgregar.grid(row=3, column=0, columnspan=2)
app = Window(root)
root.mainloop()