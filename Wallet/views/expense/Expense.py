from flask_classy import FlaskView

from flask import redirect, render_template, request, url_for

from Wallet import app
from Wallet.models import DAY, WEEK, MONTH, YEAR, Expense as ExpenseDB


class Expense(FlaskView):
    route_base = '/expense'

    def index(self):
        expenses = ExpenseDB.query.all()
        return render_template('expense.html', expenses=expenses)

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

        expense = ExpenseDB()
        expense.name = request.form['name']
        expense.amount_per_year = amount_per_year
        expense.pro_rated = pro_rated
        app.db.session.add(expense)
        app.db.session.commit()

        return redirect(url_for('Expense:index'))
