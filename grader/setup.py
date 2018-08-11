#!/usr/bin/env python3

from model import db, Grade 

db.connect()
db.create_tables([Grade])
