from abc import ABC, abstractmethod

class Animal(ABC):

    def __init__(self, nombre:str, edad:int, costo_manutension:float):
        if not isinstance(nombre, str) or nombre == "" or nombre.isspace():
            raise Exception("El nombre debe ser un string")
        if not isinstance(edad, int) or edad < 0:
            raise Exception("La edad debe ser un número positivo")
        if not isinstance(costo_manutension, (int, float)) or costo_manutension < 0:
            raise Exception("El costo de manutención debe ser un número positivo")
        self._nombre = nombre
        self._edad = edad
        self._costo_manutension = costo_manutension

    @abstractmethod
    def obtenerPrecio(self):
        pass

    def obtenerNombre(self):
        return self._nombre
    
    def obtenerEdad(self):
        return self._edad
    
    def obtenerCostoManutension(self):
        return self._costo_manutension
    
    def establecerNombre(self, nombre:str):
        if not isinstance(nombre, str):
            raise ValueError("El nombre debe ser un string")
        self._nombre = nombre

    def establecerEdad(self, edad:int):
        if not isinstance(edad, int) or edad < 0:
            raise ValueError("La edad debe ser un número positivo")
        self._edad = edad

    def establecerCostoManutension(self, costo:float):
        if not isinstance(costo, (int, float)) or costo < 0:
            raise ValueError("El costo de manutención debe ser un número positivo")
        self._costo_manutension = costo
        """Incrementa el stock de la bebida en la cantidad indicada y actualiza el costo de reposición"""
        if not isinstance(cantidad, int) or cantidad <= 0:
            raise ValueError("La cantidad debe ser un número entero positivo")
        if not isinstance(costo_reposicion, (int, float)) or costo_reposicion < 0:
            raise ValueError("El costo de reposición debe ser un número positivo")
        self._stock += cantidad
        self._costo = costo_reposicion
