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


# Crear el objeto de la familia Jackson
jackson_family = FamilyStructure("Jackson")
   
John = {
        "first_name": "John",
        "last_name": jackson_family.last_name,
        "age": 33,
        "Lucky Numbers": [7, 13, 22]
}
Jane = {
        "first_name": "Jane",
        "last_name": jackson_family.last_name,
        "age": 35,
        "Lucky Numbers": [10, 14, 3]
}
Jimmy = {
       "first_name": "Jimmy",
       "last_name": jackson_family.last_name,
       "age": 5,    
       "Lucky Numbers": [1]
}

jackson_family.add_member(John)
jackson_family.add_member(Jane)
jackson_family.add_member(Jimmy)


# Manejar/serializar errores como un objeto JSON
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code


# generate sitemap with all your endpoints

@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def get_all_members():
    try:
        members = jackson_family.get_all_members()
    except Exception as e:
        return jsonify({"msg": "Error al obtener miembros"}), 500

    if not members: 
        return jsonify({"msg": "No hay miembros"}), 400

    return jsonify(members), 200


@app.route('/member/<int:id>', methods=['GET'])
def get_member(id):
    try:
        member = jackson_family.get_member(id)
        if member is None:
            return jsonify({"error": "Miembro no encontrado."}), 404  # Error 404 si no se encuentra el miembro
        return jsonify(member), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400  # Error 400 para valores no válidos
    except Exception as e:
        return jsonify({"error": "Internal Server Error", "message": str(e)}), 500  # Error 500 para otros errores




@app.route('/member', methods=['POST'])
def create_member():
    member = request.json
    print("added", member)
    jackson_family.add_member(member)
    if member is not None:
        return "miembro creado", 200
    if not member or 'name' not in member:
        return jsonify({"msg": "Falta nombre del miembro"}), 400
    
    # # Obtener el cuerpo de la solicitud
    # member = request.json
    # # Verificar que el cuerpo de la solicitud contenga los datos necesarios
    # if not member or 'name' not in member:
    #     return jsonify({"msg": "Falta nombre del miembro"}), 400
    # # Agregar el nuevo miembro a la lista
    # jackson_family.add_member(member)
    # return jsonify({"msg": "miembro añadido"}), 200

   

@app.route('/member/<int:id>', methods=['DELETE'])
def delete_member(id):
    member = jackson_family.get_member(id)
 
    if member:
        jackson_family.delete_member(id)
        return jsonify({"msg": f"Miembro eliminado: {member}"}), 200
    else:
        return jsonify({"error": "Miembro no encontrado"}), 400


# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
