from datetime import datetime

from flask_classy import FlaskView, route

from flask import redirect, render_template, request, url_for

from Wallet import app
from Wallet.models import DAY, WEEK, MONTH, YEAR, Income as IncomeDB


class Income(FlaskView):
    route_base = '/income'

    def index(self):
        income = IncomeDB.query.all()
        return render_template('income.html', income=income)

    @route('delete', methods=['POST'])
    def delete(self):
        IncomeDB.query.filter(IncomeDB.id == request.form['id']).delete()
        app.db.session.commit()
        return redirect(url_for('Income:index'))

    def post(self):
        amount_per_year = float(request.form['amount'])
        pro_rated = YEAR

        if request.form['period'] == 'day':
            amount_per_year *= 365
            pro_rated = DAY
        elif request.form['period'] == 'week':
            amount_per_year *= 52
            pro_rated = WEEK
        elif request.form['period'] == 'month':
            amount_per_year *= 12
            pro_rated = MONTH

        income = IncomeDB()
        income.name = request.form['name']
        income.amount_per_year = amount_per_year
        income.pro_rated = pro_rated
        income.date_added = datetime.now()
        app.db.session.add(income)
        app.db.session.commit()

        return redirect(url_for('Income:index'))
