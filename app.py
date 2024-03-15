from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Simple endpoint returning a welcome message
@app.route('/')
def hello_world():
    return 'Hello, World from Flask!'


# A potentially vulnerable endpoint that echoes user input
@app.route('/echo', methods=['POST'])
def echo():
    data = request.get_json()
    user_input = data.get('input')
    return jsonify({"echo": user_input})

# An endpoint that fetches an external API (use a well-known API for demonstration)
@app.route('/external-api')
def external_api():
    response = requests.get('https://api.publicapis.org/entries')
    return jsonify(response.json())

# Endpoint with a deliberate security flaw for demonstration purposes
@app.route('/insecure')
def insecure():
    user_id = request.args.get('id')
    # Pretend we're crafting a SQL query without proper sanitization
    query = "SELECT * FROM users WHERE id = " + user_id
    # This line is for illustration only and does not execute any SQL
    return "Executing query: " + query

# Include a function with an unused import and variable to see if SonarCloud picks it up
import os
unused_variable = "I am not used anywhere"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
