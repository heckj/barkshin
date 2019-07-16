from flask import Flask
from flask import render_template
from flask import jsonify
from flask_jwt import JWT, jwt_required, current_identity
from werkzeug.security import safe_str_cmp

class User(object):
    def __init__(self, userid, username, password):
        self.userid = userid
        self.username = username
        self.password = password

    def __str__(self):
        return "User(id='%s')" % self.userid

USERS = [
    User(1, 'user1', 'abcxyz'),
    User(2, 'user2', 'abcxyz'),
]

USERNAME_TABLE = {u.username: u for u in USERS}
USERID_TABLE = {u.userid: u for u in USERS}

# endpoint defaults to /auth
def authenticate(username, password):
    user = USERNAME_TABLE.get(username, None)
    if user and safe_str_cmp(user.password.encode('utf-8'), password.encode('utf-8')):
        return user

def identity(payload):
    user_id = payload['identity']
    return USERID_TABLE.get(user_id, None)

app = Flask(__name__) # pylint: disable=invalid-name
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'notAtAllSecretBarkshin'
app.config['JWT_AUTH_USERNAME_KEY'] = 'username'
app.config['JWT_AUTH_PASSWORD_KEY'] = 'password'

jwt = JWT(app, authenticate, identity) # pylint: disable=invalid-name

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
