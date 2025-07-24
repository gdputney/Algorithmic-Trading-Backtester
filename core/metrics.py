# core/metrics.py

import pandas as pd


def compute_metrics(history: list):
    """
    history: list of (date, cash, total_value)
    returns: dict with returns series and metrics
    """
    # 1. Build DataFrame
    df = pd.DataFrame(history, columns=['date', 'cash', 'total_value'])
    df.set_index('date', inplace=True)

    # 2. Compute daily returns
    df['returns'] = df['total_value'].pct_change().fillna(0)

    # 3. CAGR
    # 4. Volatility
    # 5. Sharpe
    # 6. Drawdown
    # 7. Package into dict and return
    return df, {
        'CAGR': ...,
        'volatility': ...,
        'sharpe': ...,
        'max_drawdown': ...,
    }
