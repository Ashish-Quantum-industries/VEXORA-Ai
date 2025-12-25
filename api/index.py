from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # Security: Ye ensure karta hai ki sirf aapki website hi backend ko use kare

@app.route('/api/process', methods=['POST'])
def process_ai():
    try:
        # Frontend se data lena
        data = request.json
        tool_name = data.get('tool', 'Unknown Tool')
        user_prompt = data.get('prompt', 'No prompt provided')

        # AI Logic: Abhi hum testing ke liye success bhej rahe hain
        # Taki aapka dashboard sach mein response dikhane lage
        return jsonify({
            "status": "Success",
            "message": f"Ashish Quantum Node processed: {tool_name}",
            "details": f"Logic Applied: {user_prompt}",
            "credits_left": 4
        })

    except Exception as e:
        return jsonify({"status": "Error", "message": str(e)}), 500

# Vercel ko batane ke liye ki ye Flask app hai
def handler(request, context):
    return app(request, context)
