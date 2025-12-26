import os
import json
from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai

app = Flask(__name__)
CORS(app)

# VEXORA MASTER KEY
GEMINI_API_KEY = "AIzaSyC-0F-IweAYqFHjU46C7UpJyadCgs361tg"
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-pro')

@app.route('/api/process', methods=['POST', 'OPTIONS'])
def handler():
    if request.method == 'OPTIONS':
        return '', 200
        
    try:
        data = request.json
        tool_name = data.get('tool', 'VEXORA AI')
        prompt = data.get('prompt', 'Hello')

        # Google Gemini se asli response lana
        response = model.generate_content(
            f"You are VEXORA AI by Ashish Quantum Industries. Task: {prompt} for tool: {tool_name}. Give a highly professional, detailed, and realistic response."
        )

        return jsonify({
            "status": "Success",
            "message": response.text
        })

    except Exception as e:
        return jsonify({"status": "Error", "message": str(e)}), 500

# Vercel setup
def main(req):
    return app
