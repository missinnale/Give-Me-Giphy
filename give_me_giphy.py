from flask import Flask, render_template, request
import requests
import spacy
app = Flask(__name__)

API_KEY = '8iBZOOBFMSA3tX0oxmHQT45tm4M85wVb' #This would normally be an environment variable or something of the like, and not in the same file, because this is super insecure

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results')
def results():
    phrase = request.args.get('phraseInput')
    results = {}
    nlp = spacy.load('en_core_web_sm') # this is the english language processing model to use
    phrase_doc = nlp(phrase)
    for phrase in phrase_doc:
        # this check removes things that aren't nouns or verbs
        if phrase.is_stop:
            continue
        giphy_obj = requests.get('https://api.giphy.com/v1/gifs/search', params={
            "api_key": API_KEY,
            "q": phrase.text,
            "limit": 1,
        })
        results[phrase.text] = giphy_obj.json()['data'][0]['images']['original']['webp']
    return render_template('results.html', results=results)