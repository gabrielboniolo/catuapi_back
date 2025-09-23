from flask import jsonify, request
from app import app
from models import Cafes
from db import db

@app.route('/catuapi/cafes', methods=['GET'])
def get_cafes():
    cafes = Cafes.query.all()
    return jsonify([
        {
            "id": cafe.id,
            "nome": cafe.nome,
            "produtor": cafe.produtor,
            "variedade": cafe.variedade,
            "processo": cafe.processo,
            "sensorial_docura": cafe.sensorial_docura,
            "sensorial_acidez": cafe.sensorial_acidez,
            "sensorial_corpo": cafe.sensorial_corpo,
            "sensorial_amargor": cafe.sensorial_amargor
        } 
        for cafe in cafes
    ])


@app.route('/catuapi/cafes', methods=['POST'])
def post_cafes():
    data = request.json
    novo = Cafes(
        nome=data.get('nome'), 
        produtor=data.get('produtor'),
        variedade=data.get('variedade'),
        processo=data.get('processo'),
        sensorial_docura=data.get('sensorial_docura'),
        sensorial_acidez=data.get('sensorial_acidez'),
        sensorial_corpo=data.get('sensorial_corpo'),
        sensorial_amargor=data.get('sensorial_amargor')
    )
    db.session.add(novo)
    db.session.commit()
    return jsonify({"message": "Café adicionado com sucesso"}), 201


@app.route('/catuapi/cafes/<int:id>', methods=['PUT'])
def put_cafes(id):
    cafe = Cafes.query.get(id)
    if not cafe:
        return jsonify({"error": "Café não encontrado"}), 404

    data = request.json
    cafe.nome = data.get('nome', cafe.nome)
    cafe.produtor = data.get('produtor', cafe.produtor)
    cafe.variedade = data.get('variedade', cafe.variedade)
    cafe.processo = data.get('processo', cafe.processo)
    cafe.sensorial_docura = data.get('sensorial_docura', cafe.sensorial_docura)
    cafe.sensorial_acidez = data.get('sensorial_acidez', cafe.sensorial_acidez)
    cafe.sensorial_corpo = data.get('sensorial_corpo', cafe.sensorial_corpo)
    cafe.sensorial_amargor = data.get('sensorial_amargor', cafe.sensorial_amargor)

    db.session.commit()
    return jsonify({"message": "Café atualizado com sucesso"}), 200


@app.route('/catuapi/cafes/<int:id>', methods=['DELETE'])
def delete_cafes(id):
    cafe = Cafes.query.get(id)
    if not cafe:
        return jsonify({"error": "Café não encontrado"}), 404

    db.session.delete(cafe)
    db.session.commit()
    return jsonify({"message": "Café deletado com sucesso"}), 200