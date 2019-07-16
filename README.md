barkshin
========

A little playground app for hosting a site that intentionally returns specific errors for various URLS.
I'm using it to test mocking libraries.

Uses:

* virtualenv
* Flask

Setup
-----

    virtualenv .venv --clear
    source .venv/bin/activate
    pip install -r requirements.txt

Dev/Test Setup
--------------

    source .venv/bin/activate
    pip install -r dev-requirements.txt

run tests:

    py.test

Run locally
-----------

    python barkshin.py

CURL stuff
----------

    curl -X POST \
    -H "Content-Type: application/json" http://127.0.0.1:5000/auth \
    -d '{"username":"user1", "password":"abcxyz"}'

Heroku App
----------

setup:

    heroku create barkshin

    Creating ⬢ barkshin... done
    https://barkshin.herokuapp.com/ | https://git.heroku.com/barkshin.git

    git push heroku master
    heroku logs
    heroku open

* [Heroku python docs](https://devcenter.heroku.com/categories/python-support)
