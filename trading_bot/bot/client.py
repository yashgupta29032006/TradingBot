import os
import logging
from binance.client import Client
from binance.exceptions import BinanceAPIException
from dotenv import load_dotenv

# Load environment variables from .env if it exists
load_dotenv()

def get_futures_client():
    """
    Initialize and return a Binance Futures Testnet client.
    API keys are loaded from environment variables:
    BINANCE_API_KEY and BINANCE_API_SECRET
    """
    api_key = os.getenv('BINANCE_API_KEY')
    api_secret = os.getenv('BINANCE_API_SECRET')

    if not api_key or not api_secret:
        logging.error("API keys missing. Set BINANCE_API_KEY and BINANCE_API_SECRET environment variables.")
        raise ValueError("API keys not found in environment variables.")

    try:
        # Initializing client for Testnet
        client = Client(api_key, api_secret, testnet=True)
        logging.info("Binance Futures Testnet client initialized.")
        return client
    except Exception as e:
        logging.error(f"Failed to initialize Binance client: {str(e)}")
        raise

def handle_api_exception(e):
    """
    Handle Binance API exceptions and log them.
    """
    if isinstance(e, BinanceAPIException):
        logging.error(f"Binance API Error: Code={e.status_code}, Message={e.message}")
        return f"Binance API Error: {e.message}"
    else:
        logging.error(f"Unexpected Error: {str(e)}")
        return f"Unexpected Error: {str(e)}"
