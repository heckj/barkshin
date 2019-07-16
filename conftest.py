import pytest
from barkshin import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    testclient = app.test_client()

    with app.app_context():
        #app.init_db()
        pass

    yield testclient

    # shutdown and close up...
