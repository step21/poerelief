#!/usr/bin/env python2.7

import sys
sys.path.insert(0, "$HOME/poerelief")

from flup.server.fcgi import WSGIServer
from poerelief import app

if __name__ == '__main__':
    WSGIServer(app).run()
