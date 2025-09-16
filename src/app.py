from flask import Flask, request, render_template, send_file
import openai
import joblib
from agent import ConversationalAgent

import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Load the pre-saved model

# agent = joblib.load('src/conversational_agent_model.pkl')
agent = ConversationalAgent(api_key=os.getenv("OPENAI_API_KEY"))


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    user_input = request.form['user_input']
    response = agent.generate_response(user_input)
    return render_template('index.html', user_input=user_input, response=response)

@app.route('/download')
def download():
    # Assuming the model generates a file to be downloaded
    file_path = 'path/to/generated/file'
    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
