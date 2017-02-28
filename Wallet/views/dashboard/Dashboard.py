from flask_classy import FlaskView

from flask import render_template


class Dashboard(FlaskView):
    route_base = '/'

    def index(self):
        return render_template('dashboard.html')
