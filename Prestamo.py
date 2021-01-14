from Material import Material
from Persona import Persona
class Prestamo:
    beneficiado = Persona()
    materiales = []
    fecha = ""
    def __init__(self, name:Persona, date:str, materials:list):
        self.beneficiado = name
        self.fecha = date
        self.materiales = materials
