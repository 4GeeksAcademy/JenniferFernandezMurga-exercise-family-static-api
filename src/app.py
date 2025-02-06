"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
# Crear el objeto de la familia Jackson
jackson_family = FamilyStructure("Jackson")



# Handle/serialize errors like a JSON object
# Manejar/serializar errores como un objeto JSON
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code


# generate sitemap with all your endpoints
#Genere un mapeo del sitio con todos sus puntos finales
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def handle_hello():

    # this is how you can use the Family datastructure by calling its methods
    # así es como se puede usar la estructura de datos Family llamando a sus métodos
    #Bloque try-except para el manejo de errores
    try:
        members = jackson_family.get_all_members()
    except Exception as e:
        return jsonify({"msg": "Error al obtener miembros"}), 500

    if not members: 
        return jsonify({"msg": "No hay miembros"}), 400

    response_body = {
        "family": members
    }
    return jsonify(response_body), 200







# # @app.route('/member', methods=['POST'])
# # def add_member():

#     # request_body = request.json
#     # member.append(request_body)
#     #  jackson_family.append(request_body)
        

#     return jsonify({"msg":"miembro añadido"}), 200














# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
