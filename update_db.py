import requests as r
from base64 import b64encode
import json
import sqlalchemy as sa
import pandas as pd
from sqlalchemy import Column, String, Integer, ForeignKey, create_engine, and_, DateTime
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select
from sqlalchemy.sql.expression import update
from datetime import datetime
from . import config

header = {'Authorization' : 'Basic ' + b64encode(config.api_credentials).decode()}

url = 'https://www.mysportsfeeds.com/api/feed/pull/\
mlb/2017-regular/cumulative_player_stats.json?playerstats=AB,H,R,HR,ER'

print('Getting data...')
resp = r.get(url=url, headers=header)
print('Done.')

data = json.loads(resp.text)['cumulativeplayerstats']

players = data['playerstatsentry']

engine = create_engine(config.db_uri)

Base = declarative_base()

class player_stats(Base):
    __tablename__ = 'player_stats'
    playerid = Column(Integer, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    team = Column(String)
    homeruns = Column(Integer)
    last_updated = Column(DateTime)

class entries(Base):
    __tablename__ = 'entries'
    name = Column(String, primary_key=True)
    playerid = Column(Integer, primary_key=True)

session = sessionmaker()

session.configure(bind=engine)

s = session()

print('Loading data...')
now = str(datetime.now())
for p in players:
    upd = update(table=player_stats)\
    .where(and_(player_stats.firstname==p['player']['FirstName'],
                player_stats.lastname==p['player']['LastName'],
                player_stats.team==p['team']['Name'],))\
    .values(homeruns=p['stats']['Homeruns']['#text'], last_updated=now)
    s.execute(upd)

s.commit()

s.close()
print('Done.')
