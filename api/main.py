from flask_cors import CORS
from flask_openapi3 import OpenAPI, Info

from db import db
from routes import initialize_routes

info = Info(title="CatuAPI", version="1.0", description="API de cafés especiais")

app = OpenAPI(__name__, info=info)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///CAFES_ESPECIAIS.db'
db.init_app(app)
CORS(app)

initialize_routes(app)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
