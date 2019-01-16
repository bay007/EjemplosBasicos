class Coche:
    """Así modelaremos un coche."""

    def __init__(self, gasolina):
        self.gasolina = gasolina
        self.encendido = False
        print(f"Tenemos {gasolina} litros")

    def arrancar(self):
        if self.gasolina > 0:
            self.encendido = not self.encendido
            print("Arranca") if self.encendido else print("Apagado")
        else:
            self.encendido = False
            print("No arranca")

    def conducir(self):
        if self.gasolina > 0 and self.encendido:
            self.gasolina -= 1
            print(f"Quedan { self.gasolina} litros")
        else:
            print("No se mueve")


class CuatroXCuatro(Coche):

    def habilitar4X4(self, kilos):
        if self.encendido is True:
            self.arrancar()
            print(f"Activando 4X4 para cargar {kilos}")
            self.arrancar()
        else:
            print(f"No se puede Activar si esta apagado ")


s = CuatroXCuatro(87)
s.arrancar()
s.conducir()
s.habilitar4X4(50)
s.conducir()
s.conducir()
