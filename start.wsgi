#!/usr/bin/env python3

import sys
import six
#sys.path.insert(0, "$HOME/poerelief")
sys.path.insert(0, "/web/poeticrelief")
sys.path.insert(0, "/web/poeticrelief/poerelief")

#if six.PY2:
	#in principle flup6 should work for p2 and p3
#	from flup.server.fcgi import WSGIServer
#else:
#	from flup6.server.fcgi import WSGIServer

#with open('/tmp/pr-d.txt','w') as f:
#   f.write("foo")

from poerelief import app as application

if __name__ == '__main__':
#    WSGIServer(application).run()
    application.run()

