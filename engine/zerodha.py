from kiteconnect import KiteConnect
from config import API_KEY, API_SECRET

def get_login_url():
    kite = KiteConnect(api_key=API_KEY)
    return kite.login_url()


def generate_token(request_token):
    kite = KiteConnect(api_key=API_KEY)
    data = kite.generate_session(request_token, api_secret=API_SECRET)

    access_token = data["access_token"]
    return access_token   # ✅ Return ONLY token


def get_ltp(symbol, access_token):
    kite = KiteConnect(api_key=API_KEY)
    kite.set_access_token(access_token)

    ltp_data = kite.ltp(f"NSE:{symbol}")
    return ltp_data[f"NSE:{symbol}"]["last_price"]
