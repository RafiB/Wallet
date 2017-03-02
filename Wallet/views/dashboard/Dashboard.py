from flask_classy import FlaskView

from flask import render_template

from Wallet.models import Expense, Income, Savings


class Dashboard(FlaskView):
    route_base = '/'

    def index(self):
        savings = sum([s.amount for s in Savings.query.all()])
        income = Income.query.all()
        expenses = Expense.query.all()
        annual_income = sum([i.amount_per_year for i in income])
        annual_expenses = sum([e.amount_per_year for e in expenses])

        return render_template('dashboard.html', savings=savings,
                               income=income, expenses=expenses,
                               annual_expenses=annual_expenses,
                               daily_diff=(annual_income - annual_expenses)/365)
