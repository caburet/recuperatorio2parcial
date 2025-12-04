from modelos.entidades.animal import Animal

class Gato(Animal):
    @classmethod
    def fromDiccionario(cls, diccionario:dict):
        return cls(diccionario["nombre"], diccionario["edad"], diccionario["costo_manutension"], diccionario["color_pelaje"])

    def __init__(self, nombre:str, edad:int, costo_manutension:float, color_pelaje: str):
        super().__init__(nombre, edad, costo_manutension)
        if not isinstance(color_pelaje, str) or not color_pelaje.strip():
            raise ValueError("El color del pelaje debe ser un string y no puede estar vacío")
        self.__color_pelaje = color_pelaje

    def obtenerPrecio(self):
        return self._costo_manutension * 1.3
    
    def obtenerColorPelaje(self):
        return self.__color_pelaje
    
    def establecerColorPelaje(self, color_pelaje:str):
        if not isinstance(color_pelaje, str) or not color_pelaje.strip():
            raise ValueError("El color del pelaje debe ser un string y no puede estar vacío")
        self.__color_pelaje = color_pelaje

    def toDiccionario(self):
        return {
            "nombre": self._nombre,
            "edad": self._edad,
            "costo_manutension": self._costo_manutension,
            "color_pelaje": self.__color_pelaje,
            "precio_adopcion": self.obtenerPrecio()
        }
            "graduacionAlcoholica": self.__graduacionAlcoholica,
            "precio": self.obtenerPrecio()
        }