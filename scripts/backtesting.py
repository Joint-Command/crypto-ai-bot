import pandas as pd

class Backtester:
    def __init__(self, historical_data):
        self.data = pd.read_csv(historical_data)

    def run_strategy(self, strategy_function):
        balance = 10000  # Starting balance
        for index, row in self.data.iterrows():
            action = strategy_function(row)
            if action == "BUY":
                balance -= row['price']
            elif action == "SELL":
                balance += row['price']
        return balance

# Example strategy: Buy when price is below 50, sell when above 70
def sample_strategy(row):
    if row['price'] < 50:
        return "BUY"
    elif row['price'] > 70:
        return "SELL"
    return "HOLD"

# Example Usage
if __name__ == "__main__":
    backtester = Backtester("data/historical_prices.csv")
    final_balance = backtester.run_strategy(sample_strategy)
    print(f"Final Balance: ${final_balance:.2f}")
