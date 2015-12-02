import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from Top52 import *

DATABASE='/var/www/hosted.thiamshui.net/giggle/giggle.db'
SECRET_KEY='k9rje8ehr8'
USERNAME='admin'
PASSWORD='rier8erer'

app = Flask( __name__ )
app.config.from_object( __name__ )


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

@app.route('/searchold', methods=['POST'])
def searchold():
  C, D, Collocs = corpora()
  if " " not in request.form.get('q'):
    results = find5( request.form.get('q'), C )
  else:
    words = request.form.get('q').split(" ",1)
    list1 = find10(words[0],C)
    list2 = find10(words[1],C)
    results = choosecolloc5(list1,list2,Collocs)

  return render_template('results.html', suggestions=results, query=request.form.get('q') )

@app.route('/search', methods=['POST'])
def search2():
  from Top53 import find5,corpora
  C = corpora()
  terms = request.form.get('q').split()
  a = [ find5(t, C) for t in terms ]
  results = [ " ".join(zip(*a)[0]), " ".join(zip(*a)[1]), " ".join(zip(*a)[2]), " ".join(zip(*a)[3]), " ".join(zip(*a)[4]) ]
  return render_template('results.html', suggestions=results, query=request.form.get('q') )
    
@app.route('/save', methods=['POST'])
def save():
  cur = g.db.execute('insert into entries(query,result1,result2,result3,result4,result5,rating1,rating2,rating3,rating4,rating5) values(?,?,?,?,?,?,?,?,?,?,?)',[ request.form['query'], request.form['result0'],request.form['result1'],request.form['result2'],request.form['result3'],request.form['result4'],request.form['rating0'],request.form['rating1'],request.form['rating2'],request.form['rating3'],request.form['rating4'] ] )
  g.db.commit()
  return redirect("https://www.google.co.uk/search?q=" + request.form['query'],code=302)

@app.route('/')
def index():
  return render_template('main.html')

@app.route('/viewsearch')
def viewsearch():
  cur = g.db.execute('select * from entries')
  return render_template('view.html',results=cur)

if __name__ == '__main__':
  app.run( host='0.0.0.0' )
