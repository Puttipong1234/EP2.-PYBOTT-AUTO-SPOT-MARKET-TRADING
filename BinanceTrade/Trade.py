from binance.client import Client

try : 
    from config_dev import API_BINANCE_KEY , API_BINANCE_SECRET
except Exception:
    from config_prod import API_BINANCE_KEY , API_BINANCE_SECRET

client = Client( API_BINANCE_KEY , API_BINANCE_SECRET )