#/bin/python

from bottle import route, run, debug, template, request, validate, static_file
from pprint import pprint
import simplejson
import urllib

ECHONEST_KEY = 'YBBLFZVQBRPQF1VKS'
ECHONEST_API = 'http://developer.echonest.com/api/v4/song/search'

class EchonestMagicError(Exception):
  pass

@route('/echonest_magic', method='GET')
def echonest_magic():
  # TODO: grab phone data
  x_coordinate = request.GET.get('x_coordinate', '').strip()
  y_coordinate = request.GET.get('y_coordinate', '').strip()
  z_coordinate = request.GET.get('z_coordinate', '').strip()
  timestamp = request.GET.get('timestamp', '').strip()
  gps_location = request.GET.get('gps_location', '').strip()

  args = {\
    'api_key' : ECHONEST_KEY,\

    # limit songs to those found in 7digital catalog
    'bucket'  : 'id:7digital-US',\
    'limit'   : 'true',\

    # TODO: our own magic parameters
    'artist'  : 'Calvin Harris',\
  }

  url = ECHONEST_API + '?' + urllib.urlencode(args) + '&bucket=tracks'
  
  result = simplejson.load(urllib.urlopen(url))

  echonest_status = result['response']['status']
  if echonest_status['code'] != 0:
    print 'Error querying Echonest:', echonest_status['message']
    raise EchonestMagicError

  pprint(result)
  songs = result['response']['songs']

  return template('song_dump', songs=songs)

@route('/static/:filename')
def server_static(filename):
  return static_file(filename, root='./static/')

debug(True)
run(reloader=True, port=5888)