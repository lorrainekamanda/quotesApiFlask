#! /usr/bin/env python

from app import app

from app.model import User, Post



if __name__=='__main__':
    app.run(debug=True)
