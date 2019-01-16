"""
Se ha trabajado en un juego de picinas de patos niños; SimUDuck.
El juego muestra una larga variedad de patos nadando y graznando.
Los desarrolladores usaron POO y crearon una superclase "Duck" de la
cual todas las demás clases heredan.
"""
from abc import ABC, abstractmethod


class Duck(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def quack(self):
        pass

    @abstractmethod
    def swim(self):
        pass

    @abstractmethod
    def display(self):
        pass

    @abstractmethod
    def fly(self):
        pass


class MallardDuck(Duck):
    def __init__(self):
        pass

    def quack(self):
        pass

    def swim(self):
        pass

    def display(self):
        print("MallardDuck: Ejemplar cabeza verde")

    def fly(self):
        print("MallardDuck: 33 aleteos por minuto")


class RedHeadDuck(Duck):
    def __init__(self):
        pass

    def quack(self):
        pass

    def swim(self):
        pass

    def display(self):
        print("RedHeadDuck : Ejemplar cabeza roja")

    def fly(self):
        print("RedHeadDuck : 40 aleteos por minuto")


class RubberDuck(Duck):

    def __init__(self):
        pass

    def quack(self):
        print("RubberDuck: Silvido")

    def swim(self):
        pass

    def display(self):
        print("RubberDuck : Ejemplar amarillo")

    def fly(self):
        print("RubberDuck : 0 aleteos por minuto")


mallard = MallardDuck()
mallard.display()

red_head = RedHeadDuck()
rubber = RubberDuck()

"""
Después de años los ejecutivos de la compañia han decidido que es tiempo
de mejorar.
Para ellos los ejecutivos deciden que es haciendo que los patos vuelen
en el simulador aplastará a la competencia.
El programador Juan piensa: "Solo necesito agregar el método fly en la clase
base Duck  y así todos los tipos de patos heredarán de ella ¿Que tan difícil
puede ser?. Bendita POO"
"""
mallard.fly()
red_head.fly()
rubber.fly()


"""
Sin embargo la jefa prueba la aplicación y le parece una broma que los
patos de hule PUEDAN VOLAR, se ha agregado comportamiento inadecuado
a algunas SUBCLASES, ahora tenemos volando por la pantalla
objetos inanimados.
"""
rubber.quack()


"""
Y ahora para complicar todo se pide agregar un pato de señuelo para 
cacería, oops, ninguno vuela ni grazna.
"""
Interface CountFishInterface:
    "Fish counting interface"

    def oneFish():
        "Increments the fish count by one"

    def twoFish():
        "Increments the fish count by two"

    def getFishCount():
        "Returns the fish count"
