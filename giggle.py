import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from Top5 import *

DATABASE='/tmp/giggle.db'
SECRET_KEY='k9rje8ehr8'
USERNAME='admin'
PASSWORD='rier8erer'

app = Flask( __name__ )
app.config.from_object( __name__ )

C = corpora()

def connect_db():
  return sqlite3.connect( app.config['DATABASE'] )

@app.before_request
def before_request():
  g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
  db = getattr(g, 'db', None)
  if db is not None:
    db.close()

@app.route('/search', methods=['GET'])
def search():
  return find5( request.args.get('q'), C )

@app.route('/')
def index():
  return render_template('main.html')

if __name__ == '__main__':
  app.run( host='0.0.0.0', debug=True )
