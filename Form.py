from tkinter import *
import Persona as p
class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()
    def init_window(self):
        self.master.title("Prestamos")
        self.pack(fill=BOTH, expand=1)
        labelPersona = Label(self, text="Usuario")
        labelPersona.pack(side= LEFT)
        nombrePersona = Entry(self)
        nombrePersona.pack(side = RIGHT)
        labelMateriales = Label(self, text="Materiales")
        
root = Tk()
app = Window(root)
root.mainloop()