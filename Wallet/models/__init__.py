from Wallet import app

DAY = 1
WEEK = 2
MONTH = 3
YEAR = 4


class Income(app.db.Model):
    id = app.db.Column(app.db.Integer, primary_key=True)
    name = app.db.Column(app.db.String())
    amount_per_year = app.db.Column(app.db.Numeric)
    pro_rated = app.db.Column(app.db.Integer)


class Expense(app.db.Model):
    id = app.db.Column(app.db.Integer, primary_key=True)
    name = app.db.Column(app.db.String())
    amount_per_year = app.db.Column(app.db.Numeric)
    pro_rated = app.db.Column(app.db.Integer)


class Savings(app.db.Model):
    id = app.db.Column(app.db.Integer, primary_key=True)
    name = app.db.Column(app.db.String())
    amount = app.db.Column(app.db.Numeric)


class Reward(app.db.Model):
    id = app.db.Column(app.db.Integer, primary_key=True)
    name = app.db.Column(app.db.String())
    cost = app.db.Column(app.db.Numeric)
