
from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai

# Ashish Quantum Industries Master Engine
app = Flask(__name__)
CORS(app)

# VEXORA MASTER KEY
genai.configure(api_key="AIzaSyC-0F-IweAYqFHjU46C7UpJyadCgs361tg")
model = genai.GenerativeModel('gemini-1.5-pro')

@app.route('/api/process', methods=['POST'])
def handle_ai():
    try:
        # User se data lena
        data = request.get_json()
        if not data:
            return jsonify({"status": "Error", "message": "No data received"}), 400
            
        tool = data.get('tool', 'VEXORA AI')
        prompt = data.get('prompt', '')

        # Real AI Response from Gemini Pro
        response = model.generate_content(f"Act as VEXORA AI by Ashish Quantum Industries. Tool: {tool}. User Prompt: {prompt}")
        
        return jsonify({
            "status": "Success",
            "message": response.text
        })
    except Exception as e:
        return jsonify({"status": "Error", "message": str(e)}), 500

# Vercel ko batane ke liye ki ye Flask app hai
handler = app
