#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv

import bottle
from bottle import default_app, request, route, response, get, template

bottle.debug(True)

@get('/')
def index():
	return template('index.tpl')

bottle.run(host='0.0.0.0', port=argv[1])
