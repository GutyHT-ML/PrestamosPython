class Persona:
    nombre = ""
    apellido = ""
    def __init__(self, name:str=None, lname: str=None):
        self.nombre = name
        self.apellido = lname
        if name != None and lname != None:
            Personas.append(self)
    @staticmethod
    def ver_personas():
        return Personas
    @staticmethod
    def ver_persona(name):
        for x in Personas:
            if x.nombre == name:
                return x
    def eliminar_persona(self):
        index = Personas.index(Persona(self.nombre, self.apellido))
        Personas.pop(index)
        return Personas
Personas = []
