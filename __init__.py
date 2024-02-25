from flask import Flask
from . import auth, db, view
config = db.connect_to_database()
app = Flask(__name__, instance_relative_config=True)
app.secret_key = 'Security@roject!2FA'

app.config['SESSION_COOKIE_SAMESITE'] = None


app.register_blueprint(auth.bp)
app.register_blueprint(view.bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
