from flask import Flask
from flask import render_template
from flask import jsonify

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/json')
def make_json():
    return jsonify({"name": "fred", "count": 5, "valid": True})

@app.route('/badRequest')
def make_bad_request():
    return 'bad request!', 400

@app.route('/generalError')
def make_general_error():
    return 'error!', 500

@app.route('/')
def frontpage(searchword=None):

    results = []
    return render_template('base.html',
                           searchword=searchword,
                           results=results)

if __name__ == '__main__':
    app.run()
