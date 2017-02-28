#!/usr/bin/python

from flask import (
    Flask,
    render_template,
)

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config.from_object('Wallet.default_settings')

db = SQLAlchemy(app)
app.db = db


def do_register_views():
    from Wallet import views
    views.register_views()

do_register_views()


@app.errorhandler(404)
def page_not_found(e):
  ''' Custom 404 page. Muuuuch prettier. '''
  return render_template('404.html'), 404


@app.before_first_request
def init_db():
    app.db.create_all()

    app.db.session.commit()
