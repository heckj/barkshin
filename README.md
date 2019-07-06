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

Run locally
-----------

    python barkshin.py

Heroku App
----------

setup:

    heroku create barkshin

    Creating ⬢ barkshin... done
    https://barkshin.herokuapp.com/ | https://git.heroku.com/barkshin.git

    git push heroku master
    heroku logs
    heroku open

[Heroku python docs](https://devcenter.heroku.com/categories/python-support)
