from flask import jsonify, request
from app import app
from models import Cafes
from db import db

# GET (*)
@app.route('/catuapi/cafes', methods=['GET'])
def get_cafes():
    cafes = Cafes.query.all()
    return jsonify([{"id": cafe.id, "nome": cafe.nome, "produtor": cafe.produtor} for cafe in cafes])

# POST
@app.route('/catuapi/cafes/cadastro', methods=['POST'])
def post_cafes():
    data = request.json
    novo = Cafes(nome=data['nome'], produtor=data.get('produtor'))
    db.session.add(novo)
    db.session.commit()
    return jsonify({"message": "Café adicionado com sucesso"}), 201