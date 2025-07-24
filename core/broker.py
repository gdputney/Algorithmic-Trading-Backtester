
class Broker:
    def __init__(self, initial_cash=100000):
        self.cash = initial_cash
        self.positions = {}  # symbol -> shares
        self.history = []    # [(date, cash, value)]

    def buy(self, symbol, price, date, quantity):
        cost = price * quantity
        if self.cash >= cost:
            self.cash -= cost
            self.positions[symbol] = self.positions.get(symbol, 0) + quantity
            print(f"[{date}] BUY {quantity} x {symbol} @ {price:.2f}")
        else:
            print(f"[{date}] Not enough cash to buy {symbol}")

    def sell(self, symbol, price, date, quantity):
        if self.positions.get(symbol, 0) >= quantity:
            self.positions[symbol] -= quantity
            self.cash += price * quantity
            print(f"[{date}] SELL {quantity} x {symbol} @ {price:.2f}")
        else:
            print(f"[{date}] Not enough shares to sell {symbol}")

    def update(self, date, prices):
        total_value = self.cash
        for symbol, qty in self.positions.items():
            price = prices.get(symbol, 0)
            total_value += qty * price
        self.history.append((date, self.cash, total_value))

    def portfolio_value(self):
        return self.history[-1][2] if self.history else self.cash
