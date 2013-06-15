#! /usr/bin/env python
# -*- coding:utf-8 -*-

import os
import random
from flask import Flask, render_template, send_from_directory,jsonify,request,url_for
import MySQLdb
import my_database

from prettyprint import pp
#----------------------------------------
# initialization
#----------------------------------------

app = Flask(__name__)

app.config.update(
    DEBUG = True,
    )

#----------------------------------------
# controllers
#----------------------------------------

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'ico/favicon.ico')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route("/error/<message>")
def error(message):
    return render_template("error.html",message=message)

@app.route("/")
def index():
    if (not "user_id" in session):
        return render_template('index.html',logged_in=False)

    if (not "user_name" in session and "facebook_token" in session):
        data = facebook.get('/me').data
        if 'name' in data:
            session["user_name"]=data['name']
    if (not "user_name" in session):
        user_name = u"名無し"
        session["user_name"]=user_name

    return render_template('index.html',logged_in = True,user_id=session["user_id"],user_name=session["user_name"])

@app.route("/eggs")
def eggs():
    con = MySQLdb.connect(db="hatch",host="localhost",user="root")
    cur = con.cursor(MySQLdb.cursors.DictCursor)
    cur.execute("SELECT users.name as owner_name, challenge, promise from eggs INNER JOIN users on users.user_id = eggs.user_id;")
    data = cur.fetchall()
    eggs = []
    for row in data:
        eggs.append({
            "owner_name":row["owner_name"].decode("utf-8"),
            "challenge":row["challenge"].decode("utf-8"),
            "promise":row["promise"].decode("utf-8"),
        })
    return render_template('eggs/list.html',eggs = eggs)

@app.route("/eggs/prepare")
def egg_prepare():
    return render_template("eggs/prepare.html")

#----------------------------------------
# API
#----------------------------------------

@app.route("/promise/candidates",methods=["POST","GET"])
def get_promise_candidate():
    return jsonify({"candidates":[
        {"image_url":"http://hoge/hogehoge.jpg","name":"sukebo1"},
        {"image_url":"http://hoge/hogehoge.jpg","name":"sukebo2"},
        {"image_url":"http://hoge/hogehoge.jpg","name":"sukebo3"}]
    })

@app.route("/eggs/generate",methods=["POST","GET"])
def generate_egg():
    #insert to DB
    if (not "user_id" in session):
        return render_template('index.html',logged_in=False)

    user_id = session["user_id"]
    egg_id = random.randint(10000,100000000)
    challenge = request.values["challenge"]
    promise = request.values["promise"]
    print "parames = %d,%d,%s,%s"%(user_id,egg_id,challenge,promise)
    con = MySQLdb.connect(db="hatch",host="localhost",user="root")
    cur = con.cursor(MySQLdb.cursors.DictCursor)
    cur.execute("INSERT INTO eggs (user_id,egg_id,challenge,promise) values (%s,%s,%s,%s)",
        (user_id,egg_id,challenge,promise))
    con.commit()
    return redirect("/eggs")


#----------------------------------------
# facebook authentication
#----------------------------------------

from flask import url_for, request, session, redirect
from flask_oauth import OAuth

FACEBOOK_APP_ID = '484181624992176'
FACEBOOK_APP_SECRET = 'f2e41b1748248a6a2009ba7bb2e09efc'
app.secret_key = 'A0Zr98j/3yX R~XHH!endornodfnsofdsa'

oauth = OAuth()

facebook = oauth.remote_app('facebook',
                            base_url='https://graph.facebook.com/',
                            request_token_url=None,
                            access_token_url='/oauth/access_token',
                            authorize_url='https://www.facebook.com/dialog/oauth',
                            consumer_key=FACEBOOK_APP_ID,
                            consumer_secret=FACEBOOK_APP_SECRET,
                            request_token_params={'scope': ('email, ')}
)

@facebook.tokengetter
def get_facebook_token():
    return session.get('facebook_token')

def pop_login_session():
    session.pop('logged_in', None)
    session.pop('facebook_token', None)
    session.pop('user_name',None)
    session.pop('user_id',None)

@app.route("/dummy_login")
def dummy_login():
    session['logged_in'] = True
    user_id = request.values.get("user_id",None)
    if user_id is None:
        return redirect(url_for('error',message="No user id"))
    user_name = request.values.get("user_name","ダミーの名前")
    session['user_id'] = user_id
    session['user_name'] = user_name
    my_database.upsert_new_user(user_id,user_name)
    return redirect("/")


@app.route("/facebook_login")
def facebook_login():
    return facebook.authorize(callback=url_for('facebook_authorized',
                                               next=request.args.get('next'), _external=True))

@app.route("/facebook_authorized")
@facebook.authorized_handler
def facebook_authorized(resp):
    next_url = request.args.get('next') or url_for('index')
    if resp is None or 'access_token' not in resp:
        return redirect(next_url)

    session['logged_in'] = True
    session['facebook_token'] = (resp['access_token'], '')

    #create new user if user_id is new
    data = facebook.get('/me').data
    if 'id' in data and 'name' in data:
        user_name = data['name']
        user_id = data['id']
        session["user_name"]=user_name
        session["user_id"]=user_id
        my_database.upsert_new_user(user_id,user_name)
    else:
        return redirect(url_for('error',message="can't get facebook id or name"))

    print "access token set:",resp['access_token']
    return redirect(next_url)

@app.route("/logout")
def logout():
    pop_login_session()
    return redirect(url_for('index'))

#----------------------------------------
# launch
#----------------------------------------

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 80))
    app.run(host='127.0.0.1', port=port)


if __name__ == '__main__':
    app.run()
