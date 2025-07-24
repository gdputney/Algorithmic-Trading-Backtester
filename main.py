from strategies.sma_crossover import SMACrossoverStrategy
from core.broker import Broker
from core.backtester import Backtester
import pandas as pd

data = pd.read_csv("data/sp500/AAPL.csv", parse_dates=['Date'], index_col='Date')

strategy = SMACrossoverStrategy(symbol="AAPL")
broker = Broker(initial_cash=100000)
backtester = Backtester(data, strategy, broker)

backtester.run()

print("Final Portfolio Value:", broker.portfolio_value())
