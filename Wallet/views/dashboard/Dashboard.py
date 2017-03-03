import math

from datetime import datetime

from flask_classy import FlaskView

from flask import g, render_template

from Wallet.models import Expense, Income, Reward, Savings


def format_time_string(years, months, weeks, days):
    time_string = []
    if years:
        time_string.append('{} year{}'.format(years, 's' if years > 1 else ''))
    if months:
        time_string.append('{} month{}'.format(months, 's' if months > 1 else ''))
    if weeks:
        time_string.append('{} week{}'.format(weeks, 's' if weeks > 1 else ''))
    if days:
        time_string.append('{} day{}'.format(days, 's' if days > 1 else ''))
    return ', '.join(time_string)

class Dashboard(FlaskView):
    route_base = '/'

    def index(self):
        savings = float(sum([s.amount for s in Savings.query.all()]))
        income = Income.query.all()
        expenses = Expense.query.all()
        rewards = sorted(Reward.query.all(), key=lambda x: x.cost)
        annual_income = sum([i.amount_per_year for i in income])
        annual_expenses = sum([e.amount_per_year for e in expenses])
        daily_diff = (annual_income - annual_expenses) / 365

        savings += sum([(datetime.now() - i.date_added).total_seconds() / (60 * 60 * 24 * 365) * float(i.amount_per_year) for i in income])
        g.savings = savings

        years, months, weeks, days = 0, 0, 0, 0
        for r in rewards:
            r_years = int(r.cost / (daily_diff * 365))
            r_months = int((r.cost - (r_years * daily_diff * 365)) / (daily_diff * 31))
            r_weeks = int((r.cost - (r_years * daily_diff * 365) - (r_months * daily_diff * 31)) / (daily_diff * 7))
            r_days = int(math.ceil((r.cost - (r_years * daily_diff * 365) - (r_months * daily_diff * 31) - (r_weeks * daily_diff * 7)) / daily_diff))

            years += r_years
            months += r_months
            weeks += r_weeks
            days += r_days

            if days >= 7:
                days -= 7
                weeks += 1
            if weeks >= 4:
                weeks -= 4
                months += 1
            if months >= 12:
                months -= 12
                years += 1

            r.time_string = '{} ({})'.format(
                format_time_string(years, months, weeks, days),
                format_time_string(r_years, r_months, r_weeks, r_days))

        return render_template('dashboard.html', savings=savings,
                               income=income, expenses=expenses, rewards=rewards,
                               rewards_total=float(sum([r.cost for r in rewards])),
                               annual_expenses=annual_expenses,
                               daily_diff=daily_diff)
