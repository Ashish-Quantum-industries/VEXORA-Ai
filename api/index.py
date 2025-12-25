import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai

app = Flask(__name__)
CORS(app)

# VEXORA MASTER KEY
GEMINI_API_KEY = "AIzaSyC-0F-IweAYqFHjU46C7UpJyadCgs361tg"
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-pro')

@app.route('/api/process', methods=['POST'])
def process():
    try:
        data = request.json
        tool = data.get('tool', 'VEXORA Core')
        prompt = data.get('prompt', 'Hello')

        # Roleplaying as Ashish Quantum AI
        instructions = f"Role: VEXORA AI by Ashish Quantum Industries. Tool: {tool}. Task: {prompt}. Result must be high-end and professional."
        
        response = model.generate_content(instructions)
        
        return jsonify({
            "status": "Success",
            "message": response.text
        })
    except Exception as e:
        return jsonify({"status": "Error", "message": str(e)}), 500

# Vercel requirements
def handler(request, context):
    return app(request, context)
