from modelos.entidades.animal import Animal

class Perro(Animal):
    @classmethod
    def fromDiccionario(cls, diccionario:dict):
        return cls(diccionario["nombre"], diccionario["edad"], diccionario["costo_manutension"], diccionario["raza"])

    def __init__(self, nombre:str, edad:int, costo_manutension:float, raza: str):
        super().__init__(nombre, edad, costo_manutension)
        if not isinstance(raza, str) or not raza.strip():
            raise ValueError("La raza debe ser un string y no puede estar vacía")
        self.__raza = raza
    
    
    def obtenerRaza(self):
        return self.__raza
    
    def obtenerPrecio(self):
        return self._costo_manutension * 1.5
    
    def establecerRaza(self, raza:str):
        if not isinstance(raza, str) or raza == "":
            raise ValueError("La raza no puede estar vacía")
        self.__raza = raza

    def toDiccionario(self):
        return {
            "nombre": self._nombre,
            "edad": self._edad,
            "costo_manutension": self._costo_manutension,
            "raza": self.__raza,
            "precio_adopcion": self.obtenerPrecio()
        }
            raise ValueError("El atributo natural debe ser booleano")
        self.__natural = natural

    def obtenerPrecio(self):
        return self._costo * 1.5
    
        
    def toDiccionario(self):
        return {
            "nombre": self._nombre,
            "costo": self._costo,
            "stock": self._stock,
            "mililitros": self._mililitros,
            "sabor": self.__sabor,
            "natural": self.__natural,
            "precio": self.obtenerPrecio()
        }