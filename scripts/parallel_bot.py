import multiprocessing
import time

def start_miner():
    while True:
        print("Mining in progress...")
        time.sleep(10)

def start_trader():
    while True:
        print("AI Trading in progress...")
        time.sleep(5)

if __name__ == "__main__":
    miner_process = multiprocessing.Process(target=start_miner)
    trader_process = multiprocessing.Process(target=start_trader)

    miner_process.start()
    trader_process.start()

    miner_process.join()
    trader_process.join()
