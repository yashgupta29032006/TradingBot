import logging
from bot.client import handle_api_exception

def place_market_order(client, symbol, side, quantity):
    """
    Place a MARKET order on Binance Futures.
    """
    logging.info(f"Placing MARKET order: {symbol} {side} qty={quantity}")
    try:
        response = client.futures_create_order(
            symbol=symbol.upper(),
            side=side.upper(),
            type='MARKET',
            quantity=quantity
        )
        logging.info(f"Order response: orderId={response.get('orderId')} status={response.get('status')}")
        return response
    except Exception as e:
        error_msg = handle_api_exception(e)
        return {"error": error_msg}

def place_limit_order(client, symbol, side, quantity, price):
    """
    Place a LIMIT order on Binance Futures.
    TimeInForce is set to GTC (Good Till Cancelled) by default for limit orders.
    """
    logging.info(f"Placing LIMIT order: {symbol} {side} qty={quantity} price={price}")
    try:
        response = client.futures_create_order(
            symbol=symbol.upper(),
            side=side.upper(),
            type='LIMIT',
            quantity=quantity,
            price=str(price),
            timeInForce='GTC'
        )
        logging.info(f"Order response: orderId={response.get('orderId')} status={response.get('status')}")
        return response
    except Exception as e:
        error_msg = handle_api_exception(e)
        return {"error": error_msg}
