#!/usr/bin/python

import locale

from flask import (
    g,
    Flask,
    render_template,
)

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config.from_object('Wallet.default_settings')

db = SQLAlchemy(app)
app.db = db

locale.setlocale(locale.LC_ALL, 'en_US.utf8')


def format_currency(v):
    return locale.currency(v, grouping=True)


def generate_series(i):
    return ', '.join([str(g.savings + float(i * m)) for m in xrange(13)])

app.jinja_env.filters['format_currency'] = format_currency
app.jinja_env.filters['generate_series'] = generate_series


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
