from kiteconnect import KiteConnect
from config import API_KEY, API_SECRET

kite = KiteConnect(api_key=API_KEY)

def get_login_url():
    return kite.login_url()

def generate_token(request_token):
    data = kite.generate_session(request_token, api_secret=API_SECRET)
    kite.set_access_token(data["access_token"])
    return kite

def get_ltp(kite, symbol, exchange="NSE"):

    symbol = symbol.replace(" ", "").upper()

    if ":" not in symbol:
        symbol = f"{exchange}:{symbol}"

    try:
        ltp_data = kite.ltp(symbol)
        return ltp_data[symbol]["last_price"]
    except:
        raise Exception(f"Symbol not found: {symbol}")
