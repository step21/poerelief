#!/usr/bin/env python

import sys
import six
sys.path.insert(0, "$HOME/poerelief")

if six.PY2:
	#in principle flup6 should work for p2 and p3
	from flup.server.fcgi import WSGIServer
else:
	from flup6.server.fcgi import WSGIServer

from poerelief import app

if __name__ == '__main__':
    WSGIServer(app).run()
