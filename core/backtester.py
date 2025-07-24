#core/backtester

import pandas as pd

class Backtester:
    def __init__(self, data: pd.DataFrame, strategy, broker):
        self.data = data.copy()
        self.strategy = strategy
        self.broker = broker

    def run(self):
        signals = self.strategy.generate_signals(self.data)

        for i in range(len(self.data)):
            date = self.data.index[i]
            row = self.data.iloc[i]
            price = row['Close']
            action = signals[i]

            if action == "buy":
                self.broker.buy(self.strategy.symbol, price, date, quantity=10)
            elif action == "sell":
                self.broker.sell(self.strategy.symbol, price, date, quantity=10)

            self.broker.update(date, prices={self.strategy.symbol: price})
