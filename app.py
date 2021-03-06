#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv
from random import randint

import bottle
from bottle import default_app, request, route, response, get, post, template

bottle.debug(True)
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

def get_word(word):
	for dictionary in word_list:
		if dictionary['word'] == word:
			return dictionary


@get('/')
def index():
	return template('index.tpl')

@get('/word')
def word():

	random_index = randint(0, len(word_list) - 1)
	rand = word_list[random_index]
	
	return template('word.tpl', word = rand["word"])

@post('/word/<word>')
def check_word(word):
	user_response = request.forms.get('is-anagram')
	dictionary = get_word(word)
	if user_response == str(dictionary['is_anagram']):
		return template('result.tpl', res = "Yep, you got it!")
	else:
		return template('result.tpl', res = "Nope, try again.")


bottle.run(host='0.0.0.0', port=argv[1])
