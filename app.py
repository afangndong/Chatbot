from flask import Flask, request, jsonify
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a new chatbot instance
chatbot = ChatBot("AI Chatbot")

# Create a trainer for the chatbot
trainer = ListTrainer(chatbot)

# Train the chatbot with some basic conversation data
trainer.train([
    "Hi",
    "Hello! How can I help you?",
    "What is your name?",
    "I am an AI chatbot.",
    "How are you?",
    "I am good, thank you!",
    "Bye",
    "Goodbye!"
])

# Function to get responses from the chatbot
def get_response(user_input):
    return str(chatbot.get_response(user_input))

# Create a Flask application
app = Flask(__name__)

@app.route("/get", methods=["GET"])
def get_bot_response():
    user_input = request.args.get('msg')
    return jsonify({'response': get_response(user_input)})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)