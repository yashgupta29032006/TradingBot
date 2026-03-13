import argparse
import sys
import logging
from bot.logging_config import setup_logging
from bot.validators import (
    validate_symbol, validate_side, validate_order_type, 
    validate_quantity, validate_price, ValidationError
)
from bot.client import get_futures_client
from bot.orders import place_market_order, place_limit_order

def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Binance Futures CLI Trading Bot")
    parser.add_argument("--symbol", required=True, help="Trading symbol (e.g., BTCUSDT)")
    parser.add_argument("--side", required=True, choices=["BUY", "SELL"], help="Order side (BUY or SELL)")
    parser.add_argument("--type", required=True, choices=["MARKET", "LIMIT"], help="Order type (MARKET or LIMIT)")
    parser.add_argument("--quantity", required=True, type=float, help="Order quantity")
    parser.add_argument("--price", type=float, help="Order price (required for LIMIT orders)")
    return parser.parse_args()

def main():
    # Initialize logging
    setup_logging()

    # Parse arguments
    args = parse_args()

    try:
        # 1. Validate inputs
        validate_symbol(args.symbol)
        validate_side(args.side)
        validate_order_type(args.type)
        validate_quantity(args.quantity)
        if args.type == "LIMIT":
            if args.price is None:
                raise ValidationError("Price is required for LIMIT orders.")
            validate_price(args.price, args.type)

        # Print Order Request Summary
        print("\n--- Order Request Summary ---")
        print(f"Symbol: {args.symbol.upper()}")
        print(f"Side: {args.side.upper()}")
        print(f"Type: {args.type.upper()}")
        print(f"Quantity: {args.quantity}")
        if args.price:
            print(f"Price: {args.price}")
        print("-----------------------------\n")

        # 2. Get client
        client = get_futures_client()

        # 3. Place order
        if args.type.upper() == "MARKET":
            response = place_market_order(client, args.symbol, args.side, args.quantity)
        else:
            response = place_limit_order(client, args.symbol, args.side, args.quantity, args.price)

        # 4. Handle response
        if "error" in response:
            print(f"ERROR: {response['error']}")
            sys.exit(1)

        # Print Order Response Details
        print("--- Order Response Details ---")
        print(f"orderId: {response.get('orderId')}")
        print(f"status: {response.get('status')}")
        print(f"executedQty: {response.get('executedQty')}")
        
        # Determine avgPrice (avgPrice is often in 'avgPrice' or 'price' depending on execution)
        avg_price = response.get('avgPrice', '0.00')
        if avg_price == '0.00' and response.get('status') == 'FILLED':
           # For some versions/responses price might be 0 but fills exist
           pass 
        print(f"avgPrice: {avg_price}")
        print("------------------------------\n")

        print("SUCCESS: Order placed successfully")

    except ValidationError as e:
        print(f"ERROR: Invalid input - {str(e)}")
        sys.exit(1)
    except Exception as e:
        logging.error(f"Application error: {str(e)}")
        print(f"ERROR: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
