from flask import Flask
from flask import render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
@app.route('/<searchword>')
def frontpage(searchword=None):

    results = []
    return render_template('base.html',
                           searchword=searchword,
                           results=results)
