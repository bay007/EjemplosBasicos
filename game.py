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


class MallardDuck(Duck):
    def __init__(self):
        pass

    def quack(self):
        pass

    def swim(self):
        pass

    def display(self):
        print("Ejemplar cabeza verde")


class RedHeadDuck(Duck):
    def __init__(self):
        pass

    def quack(self):
        pass

    def swim(self):
        pass

    def display(self):
        print("Ejemplar cabeza roja")


MallardDuck()
