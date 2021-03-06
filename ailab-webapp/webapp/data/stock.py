import pandas as pd
import numpy as np
from yahoo_fin import stock_info
from typing import List
import yfinance


def get_hist_stock_price(tickers, start_date, end_date):
    result = pd.DataFrame(columns=tickers)
    for ticker in tickers:
        result[ticker] = yfinance.download(ticker, period='3m',interval='1m')['Adj Close'].tail(1)

    result['date'] = result.index
    result['date'] = result['date'].dt.strftime('%Y-%m-%d')
    result.reset_index(inplace=True, drop=True)
    return result


def get_single_hist_price(ticker, start_date, end_date):
    result = stock_info.get_data(ticker, start_date=start_date, end_date=end_date)
    result.drop(columns=['ticker'], inplace=True)
    result['date'] = result.index
    result['date'] = result['date'].dt.strftime('%Y-%m-%d')
    result.reset_index(inplace=True, drop=True)
    return result


def get_analysis_info(ticker:str):
    return stock_info.get_analysts_info(ticker)


def get_top_gainers(time_range):
    if time_range == 'daily':
        return stock_info.get_day_gainers()
    else:
        pass


def get_top_losers(time_range):
    if time_range == 'daily':
        return stock_info.get_day_losers()
    else:
        pass


def get_basic_stats(ticker):
    df = stock_info.get_stats(ticker)
    return df.to_json(orient='records')


def get_real_time_stock_price(tickers: list):
    return [stock_info.get_live_price(ticker) for ticker in tickers]


if __name__ == '__main__':
    print(get_real_time_stock_price(['AAPL']))