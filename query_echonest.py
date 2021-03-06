#/bin/python

import json
from pprint import pprint
import sys
import urllib
from backend import echonest_api as e


def main(category):
  print 'Returning results for %s...' %  category
  track_data = e.search(category)
  for t in track_data:
    del t['preview_url'] 
    del t['album_img'] 
  pprint(remove_duplicates(track_data))

def remove_duplicates(d):
    encountered_entries = set()
    for t in d:
        if t['name'] in encountered_entries:
            d.remove(t)
        else:
            encountered_entries.add(t['name'])
    return d

# ALKJASDLKFJASLDKFJADKFJADF WHYYYY
#  f = open('song_dump.html', 'w')
#  f.write('<html><head><title>Song Dump</title></head>\n<body>\n')
#  f.write('<table>\n')
#  f.write('<tr><th>name</th><th>artist</th><th>preview_url</th><th>album_img</th></tr>\n')
#  for t in track_data:
#    f.write(u'<tr><td>' + unicode(t['name'], errors='ignore') + u'</td>'\
#            + u'<td>' + unicode(t['artist'], errors='ignore') + u'</td>'\
#            + u'<td>' + unicode(t['preview_url'], errors='ignore') + u'</td>'\
#            + u'<td>' + unicode(t['album_img'], errors='ignore') + u'</td>'\
#            + u'</tr>\n')
#  f.write('<\table>\n')
#  f.write('</body></html>')
#  f.close()


if __name__ == '__main__':
  main(sys.argv[1:][0])
