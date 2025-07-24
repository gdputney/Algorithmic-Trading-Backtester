import os
import time

import pandas as pd
import yfinance as yf

# Get save path
DATA_DIR = os.path.dirname(__file__)

def get_sp500_tickers():
    url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    df = pd.read_html(url)[0]
    return df['Symbol'].str.replace('.', '-', regex=False).tolist()

def download_and_save(symbol, start="2015-01-01", end="2024-01-01"):
    try:
        df = yf.download(symbol, start=start, end=end)
        if df.empty:
            print(f"No data for {symbol}")
            return

        path = os.path.join(DATA_DIR, f"{symbol}.csv")
        df.to_csv(path)
        print(f"{symbol} saved")
        time.sleep(1)  # Avoid rate limits
    except Exception as e:
        print(f"Failed to download {symbol}: {e}")

if __name__ == "__main__":
    tickers = get_sp500_tickers()
    print(f"Downloading {len(tickers)} S&P 500 tickers...")

    for symbol in tickers:
        download_and_save(symbol)
