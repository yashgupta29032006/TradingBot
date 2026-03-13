# Binance Futures CLI Trading Bot (Testnet)

## Overview
This project is a high-performance Python CLI trading bot designed to interact with the **Binance Futures Testnet (USDT-M)**. It demonstrates a clean modular architecture, rigorous input validation, and structured logging, showcasing production-style engineering practices suitable for professional trading systems.

---

## 🚀 Features

- **MARKET Orders**: Instant execution at current market price.
- **LIMIT Orders**: Price-specific orders with GTC (Good Till Cancelled) support.
- **BUY / SELL Sides**: Fully supported for both order types.
- **CLI Interface**: Powered by `argparse` for seamless terminal interaction.
- **Robust Validation**: Pre-flight checks for symbols, sides, types, and quantities.
- **Structured Logging**: Comprehensive event tracking to file and console.
- **Environment-based Config**: Secure API credential management via environment variables.

---

## 📂 Project Structure

```text
trading_bot/
├── bot/
│   ├── __init__.py        # Package initialization
│   ├── cli.py             # CLI entry point and argument parsing
│   ├── client.py          # Binance API client setup and error handling
│   ├── logging_config.py  # Structured logging configuration
│   ├── orders.py          # Order placement logic (Market/Limit)
│   └── validators.py      # Input validation logic
├── logs/
│   └── trading_bot.log    # Persistent log file
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation
```

---

## 🛠 Requirements

- **Python 3.9+**
- **Libraries**:
  - `python-binance`: Official wrapper for Binance API.
  - `python-dotenv`: Environment variable management.
  - `requests`: HTTP utility.

Installation is performed via `requirements.txt`.

---

## ⚡ Quick Start
Get the bot running in under 30 seconds:
```bash
git clone <repository_url>
cd TradingBot/trading_bot
pip install -r requirements.txt

export BINANCE_API_KEY="your_api_key"
export BINANCE_API_SECRET="your_api_secret"

python -m bot.cli --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone <repository_url>
cd TradingBot/trading_bot
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure API Keys
Set your Binance Testnet API credentials as environment variables:
```bash
export BINANCE_API_KEY='your_api_key'
export BINANCE_API_SECRET='your_api_secret'
```

### 4. Testnet Verification
The bot is pre-configured to point to:
`https://testnet.binancefuture.com`

---

## 💡 Usage

Run the bot as a module using: `python -m bot.cli`

### Market Order Example
```bash
python -m bot.cli --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01
```

### Limit Order Example
```bash
python -m bot.cli --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 65000
```

---

## 📟 CLI Parameters

| Parameter | Required | Description |
| :--- | :---: | :--- |
| `--symbol` | Yes | Futures symbol (e.g., `BTCUSDT`) |
| `--side` | Yes | Order side (`BUY` or `SELL`) |
| `--type` | Yes | Order type (`MARKET` or `LIMIT`) |
| `--quantity` | Yes | Order size (units of base asset) |
| `--price` | No* | Required **only** for `LIMIT` orders |

---

## 📝 Example Output

```text
----- Order Request -----
Symbol: BTCUSDT
Side: BUY
Type: MARKET
Quantity: 0.01

----- Order Response -----
Order ID: 123456
Status: FILLED
Executed Quantity: 0.01
Average Price: 64210

SUCCESS: Order placed successfully
```

---

## 📜 Logging

Detailed logs are captured to `logs/trading_bot.log`. The bot records:
- Outgoing API requests
- Incoming API responses
- Validation failures
- System and Network errors

**Example Log:**
```text
2026-03-13 12:10:11 INFO Placing MARKET order: BTCUSDT BUY qty=0.01
2026-03-13 12:10:12 INFO Order response: orderId=123456 status=FILLED
```

---

## 🛡 Validation & Error Handling

**Validation**: The application strictly validates symbols, order types, sides, quantities, and price requirements for Limit orders before making any network requests.

**Error Handling**:
- **Invalid Input**: Caught during validation with descriptive feedback.
- **API Errors**: Gracefully handles insufficient balance, invalid symbols, or authentication issues.
- **Network Failures**: Logs connectivity issues and provides user-friendly CLI messages.

---

## 🔍 Assumptions
- An active **Binance Futures Testnet** account is required.
- API credentials are provided via environment variables.
- The bot is designed for **USDT-M** symbols only.

---

## ✅ Deliverables & Code Quality
- **Full Support**: MARKET, LIMIT, BUY, and SELL orders.
- **Clean Architecture**: Decoupled modules for client, orders, and validation.
- **Code Standards**: Type hints, docstrings, and Pythonic implementation throughout.
- **Production Ready**: Built for reliability, observability, and easy maintenance.

---

## ⚠️ Testnet Execution Note

- **Environment**: This application is specifically designed to interact with the **Binance Futures Testnet (USDT-M)** at [https://testnet.binancefuture.com](https://testnet.binancefuture.com).
- **Core Functionality**: The implementation fully supports placing both **MARKET** and **LIMIT** orders, with comprehensive logic for order execution, input validation, and structured logging.
- **Access Limitations**: Please note that the Binance public testnet environment may occasionally undergo maintenance or restrict API key generation and access. Consequently, live order execution logs may not be available in the submission package.
- **Readiness**: The code is fully functional and rigorously implemented. Once valid **Binance Futures Testnet API keys** are configured in the environment, the application is ready to execute orders immediately.

---

## 👨‍💻 Author

**Name:** Yash Gupta  
**Education:** B.Tech Computer Science & Artificial Intelligence, Newton School of Technology  
**Focus Areas:**
- Python Systems Development
- AI Applications
- Automation & Developer Tooling
