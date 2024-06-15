# routes.py
from flask import redirect, url_for, session, request
from app import app, keycloak_openid

@app.route('/login')
def login():
    redirect_uri = url_for('callback', _external=True)
    return redirect(keycloak_openid.auth_url(redirect_uri))

@app.route('/callback')
def callback():
    code = request.args.get('code')
    redirect_uri = url_for('callback', _external=True)
    token = keycloak_openid.token(code=code, redirect_uri=redirect_uri)
    session['token'] = token
    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))
