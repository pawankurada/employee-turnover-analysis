from flask import Flask, render_template, request, session
from transformers import pipeline
import pandas as pd
import openai
import os
from openai.error import APIError
import time

##put your key here
OPENROUTER_API_KEY = 'RELACE WITH YOUR KEY HERE'
YOUR_SITE_URL = 'www'
YOUR_APP_NAME = 'demo'
MODEL = 'mistralai/mixtral-8x7b-instruct'

# OpenRouter API base URL
openai.api_base = "https://openrouter.ai/api/v1"
openai.api_key = OPENROUTER_API_KEY

def use_model(model_name, content, max_retries=5, max_tokens=200):
    for i in range(max_retries):
        try:
            completion = openai.ChatCompletion.create(
                extra_headers={
                    "HTTP-Referer": YOUR_SITE_URL,  # Optional, for including your app on openrouter.ai rankings.
                    "X-Title": YOUR_APP_NAME,  # Optional. Shows in rankings on openrouter.ai.
                },
                model=model_name,
                messages=[
                    {"role": "system", "content": "You are a helpful assistant. "},
                    {"role": "user", "content": content}
                ],
                max_tokens=max_tokens

            )
            return completion.choices[0].message.content
        except APIError as e:
            print(f"An error occurred: {e}. Retrying... (Attempt {i + 1}/{max_retries})")
            time.sleep(1)  # Wait for 2 seconds before retrying
    print(f"Failed after {max_retries} attempts.")
    return None

df = pd.read_csv("indeed-reviews.csv")

# Initialize Flask app
app = Flask(__name__)

# Set a secret key for session management
app.secret_key = os.urandom(24)

# Function to interact with the OpenAI model
def use_model(model_name, content, max_retries=5, max_tokens=300):
    for i in range(max_retries):
        try:
            completion = openai.ChatCompletion.create(
                model=model_name,
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": content}
                ],
                max_tokens=max_tokens
            )
            return completion.choices[0].message.content
        except APIError as e:
            print(f"An error occurred: {e}. Retrying... (Attempt {i + 1}/{max_retries})")
            time.sleep(1)  # Wait for 1 second before retrying
    print(f"Failed after {max_retries} attempts.")
    return None

# Route for home page
@app.route('/')
def home():
    if 'user_id' not in session:
        session['user_id'] = os.urandom(24).hex()  # Generate a random user ID for new users
    if 'chat_history' not in session:
        session['chat_history'] = []  # Initialize chat history for the user
    return render_template('index.html', question=None, answer=None, chat_history=session['chat_history'])

# Route for handling user input
@app.route('/ask', methods=['POST'])
def ask():
    question = request.form['question']

    dataJSON = df.loc[0:20, ['rating', 'Title', 'Content', 'Pros', 'Cons']].dropna().reset_index(drop=True).to_json()
    input_text = f"Here are job reviews with 'rating','Title','Content','Pros','Cons': {dataJSON} Please answer this question: {question} Please only show the answer in a few paragraphs and less than 150 words in total"

    # Use the language model to generate a response
    output = use_model(MODEL, input_text)
    output = output.split("\n")
    
    # Update chat history for the user
    if 'chat_history' not in session:
        session['chat_history'] = []  # Initialize chat history if not already present in session
    chat_history = session['chat_history']
    chat_history.insert(0,{"question": question, "answer": output})
    session['chat_history'] = chat_history
    
    return render_template('index.html', question=question, answer=output, chat_history=chat_history)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)