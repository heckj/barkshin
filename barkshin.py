from flask import Flask
from flask import render_template
from flask import jsonify
from flask_jwt import JWT, jwt_required, current_identity
from werkzeug.security import safe_str_cmp

class User(object):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __str__(self):
        return "User(id='%s')" % self.id

users = [
    User(1, 'user1', 'abcxyz'),
    User(2, 'user2', 'abcxyz'),
]

username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}

# endpoint defaults to /auth
def authenticate(username, password):
    user = username_table.get(username, None)
    if user and safe_str_cmp(user.password.encode('utf-8'), password.encode('utf-8')):
        return user

def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id, None)

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'notAtAllSecretBarkshin'

jwt = JWT(app, authenticate, identity)

@app.route('/json')
def make_json():
    return jsonify({"name": "fred", "count": 5, "valid": True})

@app.route('/badRequest')
def make_bad_request():
    return 'bad request!', 400

@app.route('/generalError')
def make_general_error():
    return 'error!', 500

@app.route('/protected')
@jwt_required()
def protected():
    return '%s' % current_identity

@app.route('/')
def frontpage(searchword=None):

    results = []
    return render_template('base.html',
                           searchword=searchword,
                           results=results)

if __name__ == '__main__':
    app.run()
