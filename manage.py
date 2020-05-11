#! /usr/bin/env python

from app import app

from app.model import User, Post

from app import create_app

app = create_app

if __name__=='__main__':
    app.run(debug=True)
