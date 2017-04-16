from flask import Flask, request, flash, url_for, redirect, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import logging
import json
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
db = SQLAlchemy(app)

# model declaration
class Entries(db.Model):
    __tablename__ = 'entries'
    name = db.Column(db.String, primary_key=True)
    playerid = db.Column(db.Integer, primary_key=True)

class PlayerStats(db.Model):
    __tablename__ = 'player_stats'
    playerid = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String)
    team = db.Column(db.String)
    lastname = db.Column(db.String)
    homeruns = db.Column(db.String)
    last_updated = db.Column(db.DateTime)

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}

# API endpoints
@app.route('/api/players', methods=['GET'])
def get_players():
    query = PlayerStats.query\
                 .order_by(PlayerStats.homeruns.desc()).all()
    results = {'stats' : [r.as_dict() for r in query]}
    return jsonify(results)

# TODO: convert raw query to use ORM
@app.route('/api/hybrid', methods=['GET'])
def get_players_hybrid():
    conn = get_engine().connect()
    ex_q = conn.execute('''
            select name, firstname, lastname, homeruns
            from entries e
            inner join player_stats p
            on e.playerid = p.playerid
            order by name, homeruns desc''')
    results = [{'name' : x['name'],
                'homeruns' : x['homeruns'],
                'firstname' : x['firstname'],
                'lastname' : x['lastname']} for x in ex_q]
    return jsonify({'stats': results})

# TODO: convert raw query to use ORM
@app.route('/api/usertotals', methods=['GET'])
def get_totals():
    conn = get_engine().connect()
    ex_q = conn.execute('''
            select name, sum(cast(homeruns as int)) as homeruns
            from entries e
            inner join player_stats p
            on e.playerid = p.playerid
            group by name
            order by sum(cast(homeruns as int)) desc''')
    results = [{'name' : x['name'], 'homeruns' : x['homeruns']} for x in ex_q]
    return jsonify({'stats' : results})

# helpers
# TODO: complete function
def get_json_from_query(results_obj, columns):
    return

def get_engine():
    return db.get_engine(app)

def datetime_handler(dt):
    if isinstance(dt, datetime):
        print(dt)
        return str(dt)

# URL routing
@app.route('/')
def index():
  return render_template('index.html')

@app.route('/players')
def players():
  return render_template('players.html')

@app.route('/hybrid')
def hybrid():
    return render_template('hybrid.html')

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, host='0.0.0.0')
