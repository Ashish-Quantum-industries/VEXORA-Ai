from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import sys

app = Flask(__name__)
CORS(app)

# VEXORA MASTER KEY
API_KEY = "AIzaSyC-0F-IweAYqFHjU46C7UpJyadCgs361tg"

try:
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-1.5-pro')
except Exception as e:
    print(f"AI Setup Error: {e}")

@app.route('/api/process', methods=['POST', 'OPTIONS'])
def handle_ai():
    if request.method == 'OPTIONS':
        return '', 200
        
    try:
        data = request.get_json()
        if not data:
            return jsonify({"status": "Error", "message": "Empty Data Packet"}), 400
            
        tool = data.get('tool', 'VEXORA AI')
        prompt = data.get('prompt', 'System check')

        # Real AI Response
        response = model.generate_content(f"Act as VEXORA AI. Tool: {tool}. Task: {prompt}. Professional output.")
        
        return jsonify({
            "status": "Success",
            "message": response.text
        })
    except Exception as e:
        # Ye line error ko logs mein dikhayegi
        print(f"Runtime Error: {str(e)}")
        return jsonify({"status": "Error", "message": str(e)}), 500

# Vercel entry point
handler = app
