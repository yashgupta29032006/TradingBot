import logging

class ValidationError(Exception):
    """Custom exception for validation errors."""
    pass

def validate_symbol(symbol: str):
    """
    Validate that symbol is not empty and follows typical format (e.g., BTCUSDT).
    """
    if not symbol or not isinstance(symbol, str):
        logging.error(f"Validation failed: Invalid symbol '{symbol}'")
        raise ValidationError("Symbol must be a non-empty string.")
    if not symbol.isalnum():
        logging.error(f"Validation failed: Symbol '{symbol}' must be alphanumeric.")
        raise ValidationError("Symbol must be alphanumeric (e.g., BTCUSDT).")

def validate_side(side: str):
    """
    Validate order side (BUY/SELL).
    """
    valid_sides = ['BUY', 'SELL']
    if side.upper() not in valid_sides:
        logging.error(f"Validation failed: Invalid side '{side}'")
        raise ValidationError(f"Side must be one of {valid_sides}")

def validate_order_type(order_type: str):
    """
    Validate order type (MARKET/LIMIT).
    """
    valid_types = ['MARKET', 'LIMIT']
    if order_type.upper() not in valid_types:
        logging.error(f"Validation failed: Invalid order type '{order_type}'")
        raise ValidationError(f"Order type must be one of {valid_types}")

def validate_quantity(quantity: float):
    """
    Validate quantity is a positive number.
    """
    try:
        qty = float(quantity)
        if qty <= 0:
            raise ValueError
    except (ValueError, TypeError):
        logging.error(f"Validation failed: Invalid quantity '{quantity}'")
        raise ValidationError("Quantity must be a positive number.")

def validate_price(price: float, order_type: str):
    """
    Validate price for LIMIT orders.
    """
    if order_type.upper() == 'LIMIT':
        try:
            p = float(price)
            if p <= 0:
                raise ValueError
        except (ValueError, TypeError):
            logging.error(f"Validation failed: Invalid price '{price}' for LIMIT order")
            raise ValidationError("Price must be a positive number for LIMIT orders.")
