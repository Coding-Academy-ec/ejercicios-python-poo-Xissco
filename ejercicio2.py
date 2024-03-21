class Animal:
    def __init__(self, nombre):
        self.nombre = nombre # Asigna el nombre proporcionado al atributo 'nombre'

    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        return '¡Guau!'# Devuelve el sonido de un perro (ladrido)

class Gato(Animal):
    def hacer_sonido(self):
        return '¡Miau!' # Devuelve el sonido de un gato (maullido)
