from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_openapi3 import OpenAPI, Info

from routes import initialize_routes

db = SQLAlchemy()

info = Info(title="CatuAPI", version="1.0", description="API de cafés especiais")

api = OpenAPI(__name__, info=info)

api.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///CAFES_ESPECIAIS.db'
db.init_app(api)
CORS(api)

initialize_routes(api)

if __name__ == '__main__':
    with api.app_context():
        db.create_all()
    api.run(debug=True)
