from flask import Blueprint, jsonify, request
from modelos.repositorios.repositorios import obtenerRepoDuenos
from modelos.entidades.dueno import Dueno

repo_duenos = obtenerRepoDuenos()
bp_duenos = Blueprint("bp_duenos", __name__)

# ==================== RUTAS DE DUEÑOS ====================

@bp_duenos.route("/duenos", methods=["GET"])
def listar_duenos():
    return jsonify([d.toDiccionario() for d in repo_duenos.obtenerDuenos()])

@bp_duenos.route("/duenos/<string:dni>", methods=["GET"])
def obtener_dueno(dni):
    dueno = repo_duenos.obtenerDuenoPorDNI(dni)
    if dueno is None:
        return jsonify({"error": "Dueño no encontrado"}), 404
    return jsonify(dueno.toDiccionario())

@bp_duenos.route("/duenos", methods=["POST"])
def agregar_dueno():
    datos = request.json
    try:
        dueno = Dueno.fromDiccionario(datos)
        repo_duenos.agregarDueno(dueno)
        return jsonify({"Mensaje": f"Dueño agregado con éxito.", "dueno": dueno.toDiccionario()}), 201
    except (ValueError, KeyError) as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@bp_duenos.route("/duenos/<string:dni>", methods=["PUT"])
def modificar_dueno(dni):
    datos = request.json
    try:
        dueno_nuevo = Dueno.fromDiccionario(datos)
        # No permitimos modificar DNI, Repositorio lo valida también
        if repo_duenos.actualizarDueno(dni, dueno_nuevo):
            return jsonify({"Mensaje": "Dueño actualizado con éxito.", "dueno": dueno_nuevo.toDiccionario()})
        return jsonify({"error": "No se encontró el dueño a actualizar"}), 404
    except (ValueError, KeyError) as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@bp_duenos.route("/duenos/<string:dni>", methods=["DELETE"])
def eliminar_dueno(dni):
    if repo_duenos.eliminarDueno(dni):
        return jsonify({"Mensaje": "Dueño eliminado con éxito."})
    return jsonify({"error": "No se encontró el dueño a eliminar"}), 404
