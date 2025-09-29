from flask_openapi3 import Tag
from flask import jsonify
from models import Cafes
from db import db
from schemas import CafeSchema

def initialize_routes(api):
    cafe_tag = Tag(name="Cafes", description="Operações com cafés")

    @api.get("/catuapi/cafes", tags=[cafe_tag])
    def get_cafes():
        """Lista todos os cafés"""
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
            } for cafe in cafes
        ])

    @api.post("/catuapi/cafes", tags=[cafe_tag])
    def post_cafes(body: CafeSchema):
        """Adiciona um café"""
        novo = Cafes(
            nome=body.nome,
            produtor=body.produtor,
            variedade=body.variedade,
            processo=body.processo,
            sensorial_docura=body.sensorial_docura,
            sensorial_acidez=body.sensorial_acidez,
            sensorial_corpo=body.sensorial_corpo,
            sensorial_amargor=body.sensorial_amargor
        )
        db.session.add(novo)
        db.session.commit()
        return {"message": "Café adicionado com sucesso"}, 201

    @api.put("/catuapi/cafes/<int:id>", tags=[cafe_tag])
    def put_cafes(id: int, body: CafeSchema):
        """Atualiza um café"""
        cafe = Cafes.query.get(id)
        if not cafe:
            return {"error": "Café não encontrado"}, 404
        cafe.nome = body.nome
        cafe.produtor = body.produtor
        cafe.variedade = body.variedade
        cafe.processo = body.processo
        cafe.sensorial_docura = body.sensorial_docura
        cafe.sensorial_acidez = body.sensorial_acidez
        cafe.sensorial_corpo = body.sensorial_corpo
        cafe.sensorial_amargor = body.sensorial_amargor
        db.session.commit()
        return {"message": "Café atualizado com sucesso"}, 200

    @api.delete("/catuapi/cafes/<int:id>", tags=[cafe_tag])
    def delete_cafes(id: int):
        """Deleta um café"""
        cafe = Cafes.query.get(id)
        if not cafe:
            return {"error": "Café não encontrado"}, 404
        db.session.delete(cafe)
        db.session.commit()
        return {"message": "Café deletado com sucesso"}, 200
