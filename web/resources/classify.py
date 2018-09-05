#!/usr/bin/env python

from __future__ import print_function

from flask_restful import Resource
from flask import request
import requests
import subprocess
import json
import tensorflow as tf
from helper import user_exists, count_tokens, verify_pw, update_tokens_number

"""
Google: tensorflow inception v3
Under "Usage with Python API" click on "TensorFlow models repo"
Tutorials -> image -> imagenet 
Open the file classify_image.py
Copy file content
Create a new file under web with the same name and paste to it
It the file copy URL next to var DATA_URL and download the file to web folder
"""

__author__ = 'khalilj'
__creation_date__ = '09/04/2018'


class Classify(Resource):

    def post(self):
        posted_data = request.get_json()
        username = posted_data['username']
        password = posted_data['password']
        url = posted_data['url']

        if user_exists(username):
            if not verify_pw(username, password):
                return {'message': 'Wrong username or password'}, 404
        else:
            return {'Message': "Invalid username"}, 409

        if count_tokens(username) <= 0:
            return {'message': 'You are out of tokens, please refill!'}, 403

        r = requests.get(url)
        with open("temp.jpg", "wb") as f:
            f.write(r.content)
            proc = subprocess.Popen('python classify_image.py --model_dir=. --image_file=./temp.jpg',
                                    stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
            proc.communicate()[0]
            proc.wait()
            with open("text.txt") as g:
                response = json.load(g)

        update_tokens_number(username, count_tokens(username))

        """
        In the file classify_image changed in the function run_inference_on_image
        
        From:
        top_k = predictions.argsort()[-FLAGS.num_top_predictions:][::-1]
        for node_id in top_k:
            human_string = node_lookup.id_to_string(node_id)
            score = predictions[node_id]
            print('%s (score = %.5f)' % (human_string, score))
        
        
        To:
        top_k = predictions.argsort()[-FLAGS.num_top_predictions:][::-1]
        response = {}
        for node_id in top_k:
            human_string = node_lookup.id_to_string(node_id)
            score = predictions[node_id]
            response[human_string] = score
            print('%s (score = %.5f)' % (human_string, score))
        with open("text.txt") as f:
            json.dump(response, f)
        
        For the return response
        
        And imported json
        
        """
        return response
