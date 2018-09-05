#!/usr/bin/env python

from __future__ import print_function

from flask_restful import Resource
from flask import request
from helper import user_exists, count_tokens, refill_tokens

__author__ = 'khalilj'
__creation_date__ = '09/04/2018'


class Refill(Resource):

    def post(self):
        posted_data = request.get_json()
        username = posted_data['username']
        password = posted_data['admin_pw']
        refill_amount = posted_data['refill']

        if not user_exists(username):
            return {'message': 'Invalid username'}, 409

        admin_pw = "abc123"
        if not password == admin_pw:
            return {'message': 'Invalid Admin Password'}, 401  # Unauthorized

        try:
            refill_tokens(username, refill_amount + count_tokens(username))
            return {'Message': 'Refilled successfully'}, 200
        except Exception as e:
            print(e.message)
            return {'Error': e}





