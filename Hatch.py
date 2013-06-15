import os
from flask import Flask, render_template, send_from_directory
import MySQLdb
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

@app.route("/")
def index():
    if (not "facebook_token" in session):
        return render_template('index.html',logged_in=False)
    data = facebook.get('/me').data
    print data
    if 'id' in data and 'name' in data:
        user_id = data['id']
        user_name = data['name']
    return render_template('index.html',logged_in = True,user_id=user_id,user_name=user_name)
@app.route("/eggs")
def eggs():
    con = MySQLdb.connect(db="hatch",host="localhost",user="root")
    cur = con.cursor(MySQLdb.cursors.DictCursor)
    cur.execute("SELECT users.name as owner_name, content, promise from eggs INNER JOIN users;")
    data = cur.fetchall()
    eggs = []
    for row in data:
        pp(row)
        eggs.append({
            "owner_name":row["owner_name"].decode("utf-8"),
            "content":row["content"].decode("utf-8"),
            "primise":row["promise"].decode("utf-8"),
        })
    return render_template('eggs.html',eggs = eggs)


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
