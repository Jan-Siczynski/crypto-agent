# coingecko.py
import requests
from config import COINGECKO_BASE_URL, COINS, CURRENCY

def get_prices() -> dict:
    """Pobiera aktualne ceny monet."""
    url = f"{COINGECKO_BASE_URL}/simple/price"
    params = {
        "ids": ",".join(COINS),
        "vs_currencies": CURRENCY,
        "include_24hr_change": "true",
        "include_market_cap": "true",
    }
    resp = requests.get(url, params=params, timeout=10)
    resp.raise_for_status()
    return resp.json()
    # Przykład zwrotki:
    # {"bitcoin": {"usd": 67000, "usd_24h_change": 2.3, "usd_market_cap": 1.3e12}}

def get_trending() -> dict:
    """Pobiera top 7 trendujących coinsów z CoinGecko."""
    url = f"{COINGECKO_BASE_URL}/search/trending"
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()
    return resp.json()

def get_global_market() -> dict:
    """Globalne dane rynku: total market cap, dominacja BTC."""
    url = f"{COINGECKO_BASE_URL}/global"
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()
    return resp.json()