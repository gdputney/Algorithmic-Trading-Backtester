# data/download.py
import os

import yfinance as yf


def download_stock(symbol, start="2000-01-01", end="2024-01-01", filename=None):
    df = yf.download(symbol, start=start, end=end)
    
    if not filename:
        filename = f"{symbol.upper()}.csv"

    path = os.path.join(os.path.dirname(__file__), filename)
    df.to_csv(path)
    print(f" Downloaded and saved to {path}")

if __name__ == "__main__":
    download_stock("AAPL")
