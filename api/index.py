from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Ashish Quantum Industries - In-memory Database
users_db = {} 

@app.route('/api/register', methods=['POST'])
def register():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    if email in users_db:
        return jsonify({"status": "Error", "message": "Neural ID already exists."}), 400
    users_db[email] = password
    return jsonify({"status": "Success", "message": "Neural Identity Generated. Log in to Sync."})

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    if email in users_db and users_db[email] == password:
        return jsonify({"status": "Success", "message": "Neural Sync Complete."})
    return jsonify({"status": "Error", "message": "Neural Identity Invalid."}), 401

@app.route('/api/process', methods=['POST'])
def process():
    data = request.json
    tool_name = data.get('tool', 'Unknown Tool')
    return jsonify({
        "status": "Success",
        "message": f"Successfully Processed via Ashish Quantum Nodes.",
        "tool": tool_name
    })

def handler(request, context):
    return app(request, context)
