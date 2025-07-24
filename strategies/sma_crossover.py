# strategies/sma_crossover.py

import pandas as pd

class SMACrossoverStrategy:
    def __init__(self, symbol, short_window=50, long_window=200):
        self.symbol = symbol
        self.short_window = short_window
        self.long_window = long_window

    def generate_signals(self, data: pd.DataFrame):
        data = data.copy()
        data['SMA_short'] = data['Close'].rolling(window=self.short_window).mean()
        data['SMA_long'] = data['Close'].rolling(window=self.long_window).mean()

        signals = []

        for i in range(len(data)):
            if i == 0 or pd.isna(data['SMA_short'].iloc[i]) or pd.isna(data['SMA_long'].iloc[i]):
                signals.append(None)
                continue

            prev_short = data['SMA_short'].iloc[i - 1]
            prev_long = data['SMA_long'].iloc[i - 1]
            curr_short = data['SMA_short'].iloc[i]
            curr_long = data['SMA_long'].iloc[i]

            if prev_short < prev_long and curr_short > curr_long:
                signals.append("buy")
            elif prev_short > prev_long and curr_short < curr_long:
                signals.append("sell")
            else:
                signals.append(None)

        return signals
