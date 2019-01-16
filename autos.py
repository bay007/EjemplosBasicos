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


coche_juan = Coche(20)
coche_juan.arrancar()
coche_juan.conducir()
coche_juan.conducir()
coche_juan.arrancar()
coche_juan.conducir()
coche_juan.conducir()
