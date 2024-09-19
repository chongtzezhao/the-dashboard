from flask import Blueprint, request, jsonify

telebot_api_bp = Blueprint('telebot_api', __name__, url_prefix='/telebot/api')

@telebot_api_bp.route('/send', methods=['POST'])
def send_message():
    # Logic to send a message via the Telegram bot
    data = request.json
    # Process the data and send message
    return jsonify({"status": "Message sent"}), 200

@telebot_api_bp.route('/get', methods=['GET'])
def get_messages():
    # Logic to retrieve messages from the Telegram bot
    # Fetch and return messages
    return jsonify({"messages": ["Message 1", "Message 2"]}), 200