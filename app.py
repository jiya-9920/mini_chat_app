from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/message', methods=['GET'])
def get_message():
    return jsonify({"message": "Hello from backend!"})

@app.route('/api/message', methods=['POST'])
def post_message():
    data = request.json
    name = data.get("name", "Stranger")
    return jsonify({"message": f"Hello, {name}! Backend received your message."})

import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)

