from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai

app = Flask(__name__)
CORS(app)

# VEXORA MASTER KEY
genai.configure(api_key="AIzaSyC-0F-IweAYqFHjU46C7UpJyadCgs361tg")
model = genai.GenerativeModel('gemini-1.5-pro')

@app.route('/api/process', methods=['POST', 'OPTIONS'])
def handle_process():
    if request.method == 'OPTIONS':
        return '', 200
        
    try:
        data = request.json
        tool_name = data.get('tool', 'VEXORA AI')
        prompt = data.get('prompt', 'Hello')

        # Asli AI response layega Google se
        response = model.generate_content(
            f"Act as VEXORA AI by Ashish Quantum Industries. Tool: {tool_name}. Task: {prompt}. Give a high-end response."
        )

        return jsonify({
            "status": "Success",
            "message": response.text
        })

    except Exception as e:
        return jsonify({"status": "Error", "message": str(e)}), 500

# Vercel setup ke liye zaruri hai
def handler(request, context):
    return app(request, context)
