import argparse
from pprint import pprint
from typing import Dict

import pandas as pd

import requests
import psycopg2
from sqlalchemy import create_engine
from datetime import datetime

from configs import API_KEY, SYMBOLS, DB_PARAMS, TIME_INTERVAL, ENGINE_URL


def fetch_stock_prices(symbol) -> Dict:
    url = (f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}'
           f'&interval={TIME_INTERVAL}&apikey={API_KEY}')
    response = requests.get(url)
    data = response.json()
    pprint(data)
    pass


def transform_data(data, date) -> Dict:
    return {
        "date": '2024-07-26',
        "symbol": "AAPL",
        "open_price": 218.70,
        "high_price": 218.49,
        "low_price": 218.49,
        "close_price": 218.49,
        "volume": 1234567
    }


def write_to_db(data):
    connection = psycopg2.connect(**DB_PARAMS)
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO stock_data (date, symbol, open_price, high_price, low_price, close_price, volume) "
        "VALUES (%s, %s, %s, %s, %s, %s, %s)",
        (
            '2024-07-26',
            'AAPL',
            218.70,
            218.49,
            216.01,
            217.96,
            41601345
        )
    )
    connection.commit()
    cursor.close()
    connection.close()


def get_date():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--date", required=True)
    return parser.parse_args().date


def main():
    date = get_date()
    df = pd.DataFrame()
    for symbol in SYMBOLS:
        data = fetch_stock_prices(symbol)
        data = transform_data(data, date)
        df.append(data, ignore_index=True)
    engine = create_engine(ENGINE_URL)
    df.to_sql('stock_data', engine, if_exists='append', index=False)


if __name__ == '__main__':
    main()

