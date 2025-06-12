app_py = """
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import requests
import json
import asyncio
import sqlite3
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Rasa server endpoint
RASA_SERVER_URL = "http://localhost:5005/webhooks/rest/webhook"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_message = request.json.get('message')
        user_id = request.json.get('sender', 'user')
        
        # Send message to Rasa
        rasa_payload = {
            "sender": user_id,
            "message": user_message
        }
        
        response = requests.post(RASA_SERVER_URL, json=rasa_payload)
        
        if response.status_code == 200:
            rasa_response = response.json()
            
            if rasa_response:
                bot_message = rasa_response[0].get('text', 'I apologize, but I am having trouble understanding. Could you please rephrase your question?')
            else:
                bot_message = 'I apologize, but I am having trouble understanding. Could you please rephrase your question?'
        else:
            bot_message = 'Sorry, I am currently experiencing technical difficulties. Please try again later.'
        
        # Log conversation
        log_conversation(user_id, user_message, bot_message)
        
        return jsonify({'response': bot_message})
    
    except Exception as e:
        return jsonify({'response': f'Error: {str(e)}'})

@app.route('/analytics')
def analytics():
    try:
        conn = sqlite3.connect('chatbot_logs.db')
        cursor = conn.cursor()
        
        # Get interaction statistics
        cursor.execute('SELECT COUNT(*) FROM interactions')
        total_interactions = cursor.fetchone()[0] if cursor.fetchone() else 0
        
        cursor.execute('SELECT intent, COUNT(*) as count FROM interactions GROUP BY intent ORDER BY count DESC LIMIT 10')
        top_intents = cursor.fetchall()
        
        cursor.execute('SELECT AVG(confidence) FROM interactions')
        avg_confidence = cursor.fetchone()[0] if cursor.fetchone() else 0
        
        cursor.execute('SELECT COUNT(*) FROM unknown_questions')
        unknown_questions = cursor.fetchone()[0] if cursor.fetchone() else 0
        
        conn.close()
        
        analytics_data = {
            'total_interactions': total_interactions,
            'top_intents': top_intents,
            'average_confidence': round(avg_confidence, 2) if avg_confidence else 0,
            'unknown_questions': unknown_questions,
            'fallback_rate': round((unknown_questions / total_interactions * 100), 2) if total_interactions > 0 else 0
        }
        
        return jsonify(analytics_data)
    
    except Exception as e:
        return jsonify({'error': str(e)})

def log_conversation(user_id, user_message, bot_response):
    try:
        conn = sqlite3.connect('chatbot_logs.db')
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS conversations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT,
                user_message TEXT,
                bot_response TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        cursor.execute('''
            INSERT INTO conversations (user_id, user_message, bot_response)
            VALUES (?, ?, ?)
        ''', (user_id, user_message, bot_response))
        
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"Error logging conversation: {e}")

if __name__ == '__main__':
    app.run(debug=True, port=5000)
"""
