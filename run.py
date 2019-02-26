#!/usr/bin/env python
# encoding=utf-8
# run.py
from poerelief import app
print("If running in a dev environment, please go to localhost:5000 instead of 127.0.0.1:5000 as this is needed for setting/distinguishing server name")
app.run(debug = True)
