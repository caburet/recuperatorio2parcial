from modelos.entidades.gato import Gato
from modelos.entidades.perro import Perro
from modelos.entidades.animal import Animal
import json

class RepositorioAnimales:
    ruta_archivo = "datos/animales.json"

    def __init__(self):
        self.__animales = []
        self.__cargarAnimales()

    def __cargarAnimales(self):
        try:
            with open(RepositorioAnimales.ruta_archivo, "r") as archivo:
                lista_dicc_animales = json.load(archivo)
                for animal in lista_dicc_animales:
                    if "color_pelaje" in animal:
                        self.__animales.append(Gato.fromDiccionario(animal))
                    else:
                        self.__animales.append(Perro.fromDiccionario(animal))
        except FileNotFoundError:
            print("No se encontró el archivo de animales")
        except Exception as e:
            print("Error cargando los animales del archivo.\n" + str(e))

    def __guardarAnimales(self):
        try:
            with open(RepositorioAnimales.ruta_archivo, "w") as archivo:
                lista_dicc_animales = [animal.toDiccionario() for animal in self.__animales]
                json.dump(lista_dicc_animales, archivo, indent=4)
        except Exception as e:
            print("Error guardando los animales en el archivo.\n" + str(e))
    
    def obtenerAnimales(self):
        """Retorna una lista con todos los animales"""
        return self.__animales
    
    def obtenerAnimalPorNombre(self, nombre:str):
        """Retorna el animal con el nombre indicado, None si no existe"""
        for animal in self.__animales:
            if animal.obtenerNombre() == nombre:
                return animal
        return None
    
    def existeAnimal(self, nombre:str):
        """Retorna True si existe un animal con el nombre indicado, False en caso contrario"""
        return self.obtenerAnimalPorNombre(nombre) != None
    
    def agregarAnimal(self, animal: Animal):
        """Agrega un animal al repositorio si no existe uno con el mismo nombre"""
        if self.existeAnimal(animal.obtenerNombre()):
            raise Exception(f"El animal {animal.obtenerNombre()} ya existe")
        self.__animales.append(animal)
        self.__guardarAnimales()

    def actualizarAnimal(self, nombre:str, animal_nuevo: Animal):
        """Actualiza un animal existente con los datos del animal_nuevo"""
        for i, animal in enumerate(self.__animales):
            if animal.obtenerNombre() == nombre:
                self.__animales[i] = animal_nuevo
                self.__guardarAnimales()
                return True
        return False

    def eliminarAnimal(self, nombre:str):
        """Elimina un animal del repositorio"""
        for i, animal in enumerate(self.__animales):
            if animal.obtenerNombre() == nombre:
                self.__animales.pop(i)
                self.__guardarAnimales()
                return True
        return False

