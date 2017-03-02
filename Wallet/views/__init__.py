from Wallet import app

from dashboard import Dashboard
from expense import Expense
from income import Income


def register_views():
    Dashboard.register(app)
    Expense.register(app)
    Income.register(app)
