from flask import Flask, request, jsonify

app = Flask(__name__)

def unused_variable():
    unused_var = "This variable is not used anywhere"
    return "Hello, World!!"

# Simple endpoint returning a welcome message
@app.route('/')
def hello_world():
    return 'Hello, World from Flask!'

# A safe echo endpoint that only echoes back safe characters
@app.route('/echo', methods=['POST'])
def echo():
    data = request.get_json(force=True, silent=True) or {}
    user_input = data.get('input', '')
    # Simple validation to ensure that user_input only contains alphanumeric characters and spaces
    if not user_input.isalnum() and not user_input.replace(' ', '').isalnum():
        return jsonify({"error": "Invalid input"}), 400
    return jsonify({"echo": user_input})

# An endpoint that fetches an external API (use a well-known API for demonstration)
@app.route('/external-api')
def external_api():
    response = requests.get('https://api.publicapis.org/entries', timeout=5)
    # Basic error handling
    if response.ok:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Unable to fetch data from external API"}), 500

# Remove the insecure endpoint and the unused code to tidy up the application
# ...

if __name__ == '__main__':
    # Disabling debug mode for production
    app.run(host='0.0.0.0')
