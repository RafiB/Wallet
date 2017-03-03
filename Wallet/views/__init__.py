from Wallet import app

from dashboard import Dashboard
from expense import Expense
from income import Income
from reward import Reward
from savings import Savings


def register_views():
    Dashboard.register(app)
    Expense.register(app)
    Income.register(app)
    Reward.register(app)
    Savings.register(app)
