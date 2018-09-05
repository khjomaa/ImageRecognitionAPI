#!/usr/bin/env python

from __future__ import print_function

from flask import Flask
from flask_restful import Api

from resources.register import Register
from resources.classify import Classify
from resources.refill import Refill


__author__ = 'khalilj'
__creation_date__ = '09/02/2018'

app = Flask(__name__)
api = Api(app)

api.add_resource(Register, '/register')
api.add_resource(Classify, '/classify')
api.add_resource(Refill, '/refill')


@app.route('/')
def main():
    return "Hello World"


if __name__ == '__main__':
    # app.run(host='0.0.0.0', debug=True)
    app.run(host='0.0.0.0')
