#!/usr/bin/env python

from __future__ import print_function
from pymongo import MongoClient

__author__ = 'khalilj'
__creation_date__ = '09/03/2018'

client = MongoClient("mongodb://db:27017")  # To work with docker
# client = MongoClient('localhost', port=27017)  # To work locally
db = client.ImageRecognition
users = db["Users"]

