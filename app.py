# app.py
from flask import Flask, jsonify, request

app = Flask(__name__)

ITEMS = {}


@app.route('/hello', methods=['GET'])
def hello():
    return jsonify(message="Hello, World!")


@app.route('/echo', methods=['POST'])
def echo():
    data = request.get_json(force=True)
    return jsonify(data), 201


@app.route('/items/<key>', methods=['PUT'])
def put_item(key):
    data = request.get_json(force=True)
    value = data.get("value")
    ITEMS[key] = value
    return jsonify(key=key, value=value), 200


@app.route('/items/<key>', methods=['DELETE'])
def delete_item(key):
    if key in ITEMS:
        del ITEMS[key]
        return ("", 204)
    return jsonify(error="Not found"), 404


if __name__ == '__main__':
    app.run(debug=True)
