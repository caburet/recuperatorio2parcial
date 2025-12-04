from flask import Flask
from rutas.rutas_animales import bp_animales
from rutas.rutas_duenos import bp_duenos

app = Flask(__name__)

app.register_blueprint(bp_animales)
app.register_blueprint(bp_duenos)

if __name__ == "__main__":
    app.run(debug=True)
