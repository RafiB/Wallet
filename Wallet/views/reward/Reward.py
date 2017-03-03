from flask_classy import FlaskView, route

from flask import redirect, render_template, request, url_for

from Wallet import app
from Wallet.models import Reward as RewardDB


class Reward(FlaskView):
    route_base = '/reward'

    def index(self):
        rewards = RewardDB.query.all()
        return render_template('reward.html', rewards=rewards)

    @route('delete', methods=['POST'])
    def delete(self):
        RewardDB.query.filter(RewardDB.id == request.form['id']).delete()
        app.db.session.commit()
        return redirect(url_for('Reward:index'))

    def post(self):
        reward = RewardDB()
        reward.name = request.form['name']
        reward.cost = float(request.form['cost'])
        app.db.session.add(reward)
        app.db.session.commit()

        return redirect(url_for('Reward:index'))
