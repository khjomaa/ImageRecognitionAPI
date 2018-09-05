#!/usr/bin/env python

from __future__ import print_function

from flask_restful import Resource, reqparse
from flask import request
import bcrypt
import my_db
from helper import user_exists

__author__ = 'khalilj'
__creation_date__ = '09/03/2018'


class Register(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="The field username cannot be blank"
                        )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="The field password cannot be blank"
                        )

    def post(self):
        posted_data = request.get_json()
        username = posted_data['username']
        password = posted_data['password']

        if user_exists(username):
            return {'message': 'User already exists'}, 409  # 409 - Conflict

        # hashing the password
        hashed_password = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())

        my_db.users.insert({
            "Username": username,
            "Password": hashed_password,
            "Tokens": 6
        })

        return {'message': 'You successfully signed up to the API'}, 200
