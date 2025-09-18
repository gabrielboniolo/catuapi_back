from flask import jsonify
from app import app

# GET (*)
@app.route('/catuapi/cafes', methods=['GET'])
def get_cafes():
    # Passar objeto como argumento
    return jsonify()