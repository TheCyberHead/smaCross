from cyberhead.broker import Broker
from pandas import DataFrame

from backtesting.lib import crossover
from backtesting.test import GOOG


data = DataFrame
broker = Broker('Alpaca')

def iterate(broker, data):

    data.sma_10 = list(broker.prices.Close.rolling(10).mean())
    data.sma_20 = list(broker.prices.Close.rolling(20).mean())

    if crossover(data.sma_10, data.sma_20):
        broker.buy()
    elif crossover(data.sma_20, data.sma_10):
        broker.sell()
