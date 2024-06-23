from flask import Flask, request, jsonify, render_template
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer

app = Flask(__name__)

chatbot = ChatBot('MyBot')

trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train('chatterbot.corpus.english')

custom_training_data = [
    'How are you?',
    'I am good.',
    'What is your name?',
    'My name is ChatBot.'
]

trainer_custom = ListTrainer(chatbot)
trainer_custom.train(custom_training_data)

response = chatbot.get_response('Hello, how are you today?')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_response', methods=['GET'])
def get_response():
    user_input = request.args.get('msg')
    response = str(chatbot.get_response(user_input))
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
