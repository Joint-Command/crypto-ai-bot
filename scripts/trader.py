
import ccxt
import json
import os

def trade():
    with open('config/config.json', 'r') as config_file:
        config = json.load(config_file)
    
    exchange_name = config.get("exchange", "binance")
    api_key = os.getenv("API_KEY")
    secret_key = os.getenv("API_SECRET")
    
    exchange = getattr(ccxt, exchange_name)({
        'apiKey': api_key,
        'secret': secret_key,
        'enableRateLimit': True
    })
    
    balance = exchange.fetch_balance()
    print(f"Current Balance: {balance}")
    
    market = "BTC/USDT"
    ticker = exchange.fetch_ticker(market)
    price = ticker['last']
    
    if price < 50000:
        order = exchange.create_market_buy_order(market, 0.01)
    elif price > 60000:
        order = exchange.create_market_sell_order(market, 0.01)
    
    print("Trade Executed: ", order)

if __name__ == "__main__":
    trade()
