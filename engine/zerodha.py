from kiteconnect import KiteConnect
from config import API_KEY, API_SECRET

kite = KiteConnect(api_key=API_KEY)

def get_login_url():
    return kite.login_url()

def generate_token(request_token):
    data = kite.generate_session(request_token, api_secret=API_SECRET)
    kite.set_access_token(data["access_token"])
    return kite

INDEX_MAP = {
    "NIFTY": "NSE:NIFTY 50",
    "BANKNIFTY": "NSE:NIFTY BANK",
    "FINNIFTY": "NSE:NIFTY FIN SERVICE"
}

def get_ltp(kite, symbol, exchange="NSE"):
    symbol = symbol.strip().upper()

    # Handle Index names properly
    if symbol in INDEX_MAP:
        tradingsymbol = INDEX_MAP[symbol]
    else:
        tradingsymbol = f"{exchange}:{symbol.replace(' ', '')}"

    try:
        ltp_data = kite.ltp(tradingsymbol)
        return ltp_data[tradingsymbol]["last_price"]
    except Exception as e:
        raise Exception(f"Symbol not found on Zerodha: {tradingsymbol}")

