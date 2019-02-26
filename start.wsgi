#!/usr/bin/env python3

import sys

sys.path.insert(0, "/web/poeticrelief")
sys.path.insert(0, "/web/poeticrelief/poerelief")

from poerelief import app as application

if __name__ == '__main__':

    application.run()
