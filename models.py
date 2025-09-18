from db import db

class Cafes(db.Model):
    __tablename__ = 'CAFES'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    produtor = db.Column(db.String(50), nullable=False)
    #variedade = db.Column(db.String(50), nullable=False)
    #sensorial = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<{self.nome}>'