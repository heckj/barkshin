def test_json_route(client):
    rv = client.get('/')
    print(rv)
    #assert b'Barkshin' in rv.data
    assert rv.status_code == 200

def login(client, username, password):
    return client.post('/auth', data=dict(
        username=username, #user1
        password=password #abcxyz
    ), follow_redirects=True)

def test_login_auth(client):
    rv = login(client, 'user1', 'abcxyz')
    print("RV is ", rv)
    # assert b'x' in rv.data
