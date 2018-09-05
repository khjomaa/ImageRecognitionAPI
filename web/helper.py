#!/usr/bin/env python

from __future__ import print_function
import my_db
import bcrypt

__author__ = 'khalilj'
__creation_date__ = '09/04/2018'


def verify_pw(username, password):
    hashed_pw = my_db.users.find({
        "Username": username
    })[0]["Password"]

    try:
        # if bcrypt.hashpw(password.encode('utf8'), hashed_pw.encode('utf8')) == hashed_pw:
        if bcrypt.checkpw(password.encode('utf8'), hashed_pw.encode('utf8')):
            return True
        return False
    except TypeError as e:
        print("Error: ", e.message)


def count_tokens(username):
    return my_db.users.find({"Username": username})[0]["Tokens"]


def user_exists(username):
    return my_db.users.find({"Username": username}).count() > 0


def update_tokens_number(username, current_tokens):
    my_db.users.update({
        "Username": username
    }, {
        "$set": {
            "Tokens": current_tokens - 1
        }
    })


def refill_tokens(username, refill_amount):
    my_db.users.update({
        "Username": username
    }, {
        "$set": {
            "Tokens": refill_amount
        }
    })
