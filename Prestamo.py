from Material import Material as m
class Prestamo:
    Beneficiado = ""
    Materiales = [m]
    Fecha = ""
    def __init__(self, name,date, materials = []):
        self.Beneficiado = name
        self.Fecha = date
        self.Materiales = materials
