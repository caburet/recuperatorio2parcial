from flask import Blueprint, jsonify, request
from modelos.repositorios.repositorios import obtenerRepoAnimales
from modelos.entidades.bebida import Animal
from modelos.entidades.bebidaConAlcohol import Gato 
from modelos.entidades.bebidaSinAlcohol import Perro

repo_animales = obtenerRepoAnimales()


bp_bebidas = Blueprint("bp_bebidas", __name__)

# ==================== RUTAS DE ANIMALES ====================

@bp_bebidas.route("/animales", methods = ["GET"])
def listar_animales():
    return jsonify([animal.toDiccionario() for animal in repo_animales.obtenerAnimales()])

@bp_bebidas.route("/animales/<string:nombre>", methods = ["GET"])
def obtener_animal(nombre):
    animal = repo_animales.obtenerAnimalPorNombre(nombre)
    if animal == None:
        return jsonify({"error": "Animal no encontrado"}), 404
    return jsonify(animal.toDiccionario())

@bp_bebidas.route("/animales", methods = ["POST"])
def agregar_animal():
    datos = request.json
    try:
        if "color_pelaje" in datos:
            animal = Gato.fromDiccionario(datos)
            tipo = "gato"
        else:
            animal = Perro.fromDiccionario(datos)
            tipo = "perro"
        repo_animales.agregarAnimal(animal)
        return jsonify({"Mensaje":f"{tipo.capitalize()} agregado con éxito.","animal":animal.toDiccionario()}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    
@bp_bebidas.route("/animales/<string:nombre>", methods = ["PUT"])
def modificar_animal(nombre):
    datos = request.json
    try:
        if "color_pelaje" in datos:
            animal = Gato.fromDiccionario(datos)
            tipo = "gato"
        else:
            animal = Perro.fromDiccionario(datos)
            tipo = "perro"
        if repo_animales.actualizarAnimal(nombre, animal):
            return jsonify({"Mensaje":f"{tipo.capitalize()} actualizado con éxito.","animal":animal.toDiccionario()})
        return jsonify({"error": "No se encontró el animal a actualizar"}), 404
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    
@bp_bebidas.route("/animales/<string:nombre>", methods = ["DELETE"])
def eliminar_animal(nombre):
    if repo_animales.eliminarAnimal(nombre):
        return jsonify({"Mensaje":f"Animal eliminado con éxito."})
    return jsonify({"error": "No se encontró el animal a eliminar"}), 404

@bp_bebidas.route("/animales/<string:nombre>/precio", methods=["GET"])
def obtener_precio_animal(nombre):
    animal = repo_animales.obtenerAnimalPorNombre(nombre)
    if animal is None:
        return jsonify({"error": "Animal no encontrado"}), 404
    return jsonify({"nombre": animal.obtenerNombre(), "precio_adopcion": animal.obtenerPrecio()})

