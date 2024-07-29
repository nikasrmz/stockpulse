API_KEY = '277EEH7ER86SXZV0'
SYMBOLS = [
    'AAPL',
    'MSFT',
    'NVDA',
    'GOOGL',
    'AMZN',
    'META'
]

DB_PARAMS = {
    'dbname': 'stock_prices',
    'user': 'postgres',
    'password': '1191',
    'host': 'localhost'
}

ENGINE_URL = f'postgresql://{DB_PARAMS["user"]}:{DB_PARAMS["password"]}@{DB_PARAMS["host"]}/{DB_PARAMS["dbname"]}'

TIME_INTERVAL = '5min'
