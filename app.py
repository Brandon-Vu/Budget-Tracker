from flask import Flask, request, jsonify
import os
from chatbot import get_response  # Ensure chatbot.py is in the same directory

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_id = data.get("user_id")
    message = data.get("message")
    if not user_id or not message:
        return jsonify({"error": "Missing user_id or message"}), 400

    # Set the environment variable for the current session.
    os.environ["SAIVE_USER_ID"] = user_id

    # Get the chatbot response.
    response = get_response(message)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)