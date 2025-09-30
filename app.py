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

if __name__ == '__main__':
    app.run(debug=True)
