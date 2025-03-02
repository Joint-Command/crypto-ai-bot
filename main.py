
import os
import subprocess

def start_bot(wallet):
    print(f"Starting Crypto AI Bot for wallet: {wallet}")
    subprocess.Popen(["python", "scripts/miner.py"], shell=True)
    subprocess.Popen(["python", "scripts/trader.py"], shell=True)
    subprocess.Popen(["python", "dashboard/dashboard.py"], shell=True)

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3 or sys.argv[1] != "--wallet":
        print("Usage: python main.py --wallet <WALLET_ADDRESS>")
        sys.exit(1)

    wallet_address = sys.argv[2]
    start_bot(wallet_address)
