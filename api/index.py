
import os
import json
from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai

app = Flask(__name__)
CORS(app)

# VEXORA MASTER KEY (Configured)
GEMINI_API_KEY = "AIzaSyC-0F-IweAYqFHjU46C7UpJyadCgs361tg"

# Initialize Google Gemini
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-pro')

@app.route('/api/process', methods=['POST'])
def process_ai():
    try:
        data = request.json
        tool = data.get('tool', 'VEXORA Core')
        prompt = data.get('prompt', 'Initialize session')

        # Roleplay as VEXORA Intelligence
        system_instruction = f"You are VEXORA AI, a world-class autonomous intelligence engineered by Ashish Quantum Industries. Your output must be extremely professional, realistic, and detailed. Task for tool '{tool}': {prompt}"

        # Get AI Response
        response = model.generate_content(system_instruction)
        ai_output = response.text

        return jsonify({
            "status": "Success",
            "message": ai_output,
            "credits_left": 4
        })

    except Exception as e:
        return jsonify({
            "status": "Error",
            "message": "Quantum Link Interrupted. Neural Nodes Re-syncing..."
        }), 500

# Vercel Handler
def handler(request, context):
    return app(request, context)
