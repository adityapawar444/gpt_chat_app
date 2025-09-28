from flask import Flask, request, jsonify, render_template, Response
import json
from dotenv import load_dotenv

from gpt_service import get_gpt_response

load_dotenv()  # take environment variables

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    input = request.json.get('message')
    gpt_resp = get_gpt_response(input=input)
    response_data = {'reply': gpt_resp}
    return Response(
        response=json.dumps(response_data),
        status=200,
        mimetype='application/json'
    )
