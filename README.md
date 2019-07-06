barkshin
========

A little playground app for hosting a site that intentionally returns specific errors for various URLS.
I'm using it to test mocking libraries.

Uses:
* virtualenv

Setup
-----

    virtualenv .venv --clear
    source .venv/bin/activate
    pip install -r requirements.txt

Heroku App
----------

App URL http://t5concordance.herokuapp.com/
Git URL git@heroku.com:t5concordance.git

    git push heroku heroku:master
