# 🤖 Crypto Agent — AI-Powered Cryptocurrency Market Analyst

An autonomous AI agent built with Python and Claude API that automatically fetches real-time cryptocurrency data and generates professional daily market reports in Markdown.

## 📋 What It Does

The agent runs a full agentic loop using Claude's function calling:
1. Fetches current prices of BTC, ETH, and SOL from CoinGecko
2. Fetches trending coins on the market
3. Fetches global market data (market cap, BTC dominance, volume)
4. Generates a professional daily market report in Markdown

## 🛠️ Tech Stack

- **Python 3.12+**
- **Claude API** (Anthropic) — AI analyst with function calling
- **CoinGecko API** — real-time crypto market data (free, no key required)
- **JSON** — tool result serialization

## 📁 Project Structure

```
crypto_agent/
├── agent.py            # Main agent loop with function calling
├── tools.py            # Tool definitions (JSON schemas for Claude)
├── coingecko.py        # CoinGecko API integration
├── report_generator.py # Saves generated report to Markdown file
├── config.py           # API keys and settings (not included in repo)
├── requirements.txt    # Python dependencies
└── outputs/            # Generated reports saved here
```

## ⚙️ Setup

### 1. Clone the repository
```bash
git clone https://github.com/Jan-Siczynski/crypto-agent.git
cd crypto-agent
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure API key
Create a `config.py` file in the project folder:
```python
ANTHROPIC_API_KEY = "sk-ant-your-key-here"
COINGECKO_BASE_URL = "https://api.coingecko.com/api/v3"
COINS = ["bitcoin", "ethereum", "solana"]
CURRENCY = "usd"
```
Get your API key at: [console.anthropic.com](https://console.anthropic.com)

### 4. Run the agent
```bash
py agent.py
```

## 📊 Example Output

```
🤖 Agent startuje...
   Stop reason: tool_use
   🔧 Wywołuję: get_crypto_prices
   🔧 Wywołuję: get_trending_coins
   🔧 Wywołuję: get_global_market_data
   Stop reason: tool_use
   🔧 Wywołuję: generate_report
   📄 Raport zapisany: outputs/report_2026-06-28.md
   Stop reason: end_turn
✅ Agent zakończył pracę.
```

## 🔑 Environment Variables

| Variable | Description |
|---|---|
| `ANTHROPIC_API_KEY` | Your Anthropic API key |

## 📦 Requirements

```
anthropic
requests
```

Install with:
```bash
pip install anthropic requests
```

## 💡 How It Works

The agent uses Claude's **function calling** (tool use) feature. Claude decides which tools to call and in what order. The agent loop continues until Claude returns `end_turn`, meaning it has finished all tasks and generated the report.

```
User prompt
    ↓
Claude decides what tools to call
    ↓
Agent executes tools (CoinGecko API)
    ↓
Results returned to Claude
    ↓
Claude generates report
    ↓
Report saved to outputs/
```

## 🚀 Possible Extensions

- Scheduled daily runs via Windows Task Scheduler or cron
- Email delivery of the report after generation
- Telegram bot integration
- Price charts generated as images
- Support for more cryptocurrencies

## 📄 License

MIT License — free to use and modify.

## 👤 Author

**Jan Siczyński**  
GitHub: [@Jan-Siczynski](https://github.com/Jan-Siczynski)
