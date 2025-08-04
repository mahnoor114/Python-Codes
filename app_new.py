#!/usr/bin/env python
# coding: utf-8

# In[10]:


from flask import Flask, render_template, request, redirect, url_for, session
import requests
import html
import random

app = Flask(__name__)
app.secret_key = '123456'

def get_question():
    url = "https://opentdb.com/api.php?amount=1&type=multiple"
    response = requests.get(url).json()
    data = response['results'][0]

    question = html.unescape(data['question'])
    correct = html.unescape(data['correct_answer'])
    options = [html.unescape(opt) for opt in data['incorrect_answers']]
    options.append(correct)
    random.shuffle(options)

    return {
        "question": question,
        "options": options,
        "answer": correct
    }

@app.route('/')
def home():
    session['score'] = 0
    session['current_q'] = 0
    session['questions'] = []
    return render_template('home.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    # If the user submitted an answer
    if request.method == 'POST':
        selected = request.form.get('option')
        if session['questions']:  # Only evaluate if there's at least one question stored
            last_question = session['questions'][-1]
            if selected == last_question['answer']:
                session['score'] += 1
            session['current_q'] += 1

        if session['current_q'] >= 5:
            return redirect(url_for('result'))

    # Fetch a new question
    question = get_question()
    session['questions'].append(question)

    return render_template('question.html', q=question, index=session['current_q'])

@app.route('/result')
def result():
    return render_template('result.html', score=session.get('score', 0), total=5)

if __name__ == '__main__':
    app.run(debug=True)


# In[5]:


#pip install requests


# In[8]:


#pip install flask


# In[ ]:




