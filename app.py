#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv
from random import randint

import bottle
from bottle import default_app, request, route, response, get, template

bottle.debug(True)



@get('/')
def index():
	return template('index.tpl')

@get('/word')
def word():

	word_list = [
		{
			"word": "born",
			"is_anagram" : False 
		},
		{
			"word" : "blue",
			"is_anagram" : True
		}
	]
	random_index = randint(0, len(word_list) - 1)
	rand = word_list[random_index]
	
	return template('word.tpl', word = rand["word"])

bottle.run(host='0.0.0.0', port=argv[1])
