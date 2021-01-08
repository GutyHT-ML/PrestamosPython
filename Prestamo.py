import App1.Material as m
class Prestamo:
    Beneficiado = ""
    Materiales = list[m]
    Fecha = ""
    def __init__(self, name, date, materials):
        self.Beneficiado = name
        self.Materiales = materials
        self.Fecha = date
