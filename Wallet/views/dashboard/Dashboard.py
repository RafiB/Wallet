from flask_classy import FlaskView

from flask import render_template


class Dashboard(FlaskView):
    route_base = '/'

    def index(self):
        daily_diff = 213.85
        return render_template('dashboard.html', daily_diff=daily_diff)
