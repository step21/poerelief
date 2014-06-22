# encoding=utf-8

from sqlalchemy import *

class DBC(object):
    def __init__(self):
      self.type = ""

    def connect(self, type):
      engine = create_engine(type + ':///teidb.sql', echo=True)
      connection = engine.connect()
      return connection

    def disconnect(self, connection):
      if connection.close():
        return 0
      else:
        return 1

#change to metadata code?
    def loadschema(self, connection):
      connection.execute("""drop table if exists tei_entries;""")
      connection.execute("""create table tei_entries (
  id integer primary key autoincrement,
  loc text,
  url text,
  expr text,
  licence text,
  title text,
  urld text,
  date date,
  insc text,
  material text,
  condition text,
  decoration text,
  geoname text,
  geotype text,
  geocountry text,
  georegion text,
  geocoord float,
  images text,
  idd text,
  sex text,
  pname text,
  deathdate date,
  edition text,
  verso text,
  recto text,
  translation text,
  linecomm text,
  endcomm text,
  proso text,
  bibliography text
);
      """)

    def cmdata(self, conn):
      metadata = schema.MetaData()
      return metadata

    def getDBRecord(self, conn, field):
      res = conn.execute("""SELECT """ + field + """ FROM tei_entries)"""
      return res

    def setDBRecord(self, conn, field, val):
      ins = """INSERT INTO tei_entries (""" + field + """) VALUES (?);"""
      res = conn.execute(ins, val)
      return res
