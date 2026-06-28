# tools.py
# Definicje narzędzi w formacie JSON Schema — Anthropic API je rozumie

TOOLS = [
    {
        "name": "get_crypto_prices",
        "description": "Pobiera aktualne ceny BTC, ETH, SOL wraz z 24h zmianą i market cap.",
        "input_schema": {
            "type": "object",
            "properties": {},   # brak parametrów — zawsze pobiera z config.py
            "required": [],
        },
    },
    {
        "name": "get_trending_coins",
        "description": "Pobiera listę 7 najpopularniejszych (trendujących) kryptowalut z ostatnich 24h.",
        "input_schema": {
            "type": "object",
            "properties": {},
            "required": [],
        },
    },
    {
        "name": "get_global_market_data",
        "description": "Pobiera globalne dane rynku: całkowitą kapitalizację, dominację BTC, liczbę aktywnych coinsów.",
        "input_schema": {
            "type": "object",
            "properties": {},
            "required": [],
        },
    },
    {
        "name": "generate_report",
        "description": "Generuje końcowy raport rynkowy w Markdown na podstawie zebranych danych. Wywołaj jako OSTATNIE narzędzie.",
        "input_schema": {
            "type": "object",
            "properties": {
                "report_content": {
                    "type": "string",
                    "description": "Pełna treść raportu w formacie Markdown.",
                }
            },
            "required": ["report_content"],
        },
    },
]