from modelos.repositorios.repositorio_Bebidas import RepositorioAnimales


animales = None


def obtenerRepoAnimales():
    global animales
    if animales == None:
        animales = RepositorioAnimales()
    return animales

