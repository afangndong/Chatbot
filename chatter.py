from flask import Flask, request, jsonify
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a new chatbot instance
chatbot = ChatBot("KLZ Chatbot")

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
    "Tell me a joke",
    "Why don't scientists trust atoms? Because they make up everything!", 
    "Bye",
    "Goodbye!"
])


# Create a Flask application
app = Flask(__name__)


@app.route("/get", methods=["GET"])
def get_bot_response():
    user_input = request.args.get('msg')
    bot_response = str(chatbot.get_response(user_input))

    # Check if the response is a default or fallback response
    if bot_response == "I'm sorry, but I don't have an answer for that.":
        # Ask user for the correct response
        return jsonify({'response': bot_response, 'ask_for_correction': True})

    return jsonify({'response': bot_response})


@app.route("/update", methods=["POST"])
def update_bot():
    data = request.json
    new_question = data.get('question')
    correct_response = data.get('response')

    # Train the chatbot with the new question-response pair
    trainer.train([new_question, correct_response])
    
    return jsonify({'status': 'success', 'message': 'Updated successfully!'})

@app.route("/")
def home():
    return app.send_static_file('index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
