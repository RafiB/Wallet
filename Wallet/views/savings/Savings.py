from flask_classy import FlaskView, route

from flask import redirect, render_template, request, url_for

from Wallet import app
from Wallet.models import Savings as SavingsDB


class Savings(FlaskView):
    route_base = '/savings'

    def index(self):
        savings = SavingsDB.query.all()
        return render_template('savings.html', savings=savings)

    @route('delete', methods=['POST'])
    def delete(self):
        SavingsDB.query.filter(SavingsDB.id == request.form['id']).delete()
        app.db.session.commit()
        return redirect(url_for('Savings:index'))

    def post(self):
        savings = SavingsDB()
        savings.name = request.form['name']
        savings.amount = float(request.form['amount'])
        app.db.session.add(savings)
        app.db.session.commit()

        return redirect(url_for('Savings:index'))
