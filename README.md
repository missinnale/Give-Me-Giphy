To run this you first need to be on a virtual environment. And need the following installed:
 - Flask
 - Requests
 - Spacy

This can be done via `pip install`.

Normally these would be contained in a requirements file to which you could just pip install all requirements from, but I haven't gotten to that here.

Once that is complete you need to do the following to make sure spacey can function:
```bash
python -m spacy download en_core_web_sm
```

Then in your terminal, assuming you're using Unix/Linux, you want to:
```bash
export FLASK_APP=give_me_giphy.py
```

And then to spin up the server locally to check it out run:
```bash
flask run
```

Enjoy!

P.S. I used the following tutorial for the addition of spacy to rule out non nouns and verbs: https://realpython.com/natural-language-processing-spacy-python/
