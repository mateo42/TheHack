import bottle
from bottle import template, static_file, request
from settings import STATIC_PATH

FRONT_END = bottle.Bottle()

@FRONT_END.route( '/index' )
def front_end_index():
	login = True
	s = bottle.request.environ.get('beaker.session')

	if s:
		username = s.get('username')
	else:
		username = None

	if username:
		login = False

	return template('index', login=login, username=username)