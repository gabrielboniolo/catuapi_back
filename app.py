from flask import Flask
# from flask_cors import CORS
# from flask_sqlalchemy import SQLALCHEMY()

app = Flask(__name__)
#CORS(app)

from routes import *

if __name__ == '__main__':
    app.run()