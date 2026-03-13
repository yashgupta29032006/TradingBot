import logging
import os

def setup_logging():
    """
    Configure structured logging for the trading bot.
    Logs are written to both 'logs/trading_bot.log' and the console.
    """
    log_dir = 'logs'
    log_file = os.path.join(log_dir, 'trading_bot.log')

    # Create logs directory if it doesn't exist
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Configure logging format
    log_format = '%(asctime)s %(levelname)s %(message)s'
    date_format = '%Y-%m-%d %H:%M:%S'

    logging.basicConfig(
        level=logging.INFO,
        format=log_format,
        datefmt=date_format,
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )

    logging.info("Logging initialized.")
