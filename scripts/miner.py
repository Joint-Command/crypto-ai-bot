
import os
import json
import subprocess

def start_mining(wallet):
    with open('config/config.json', 'r') as config_file:
        config = json.load(config_file)
    
    mining_algorithm = config.get("mining_algorithm", "auto")
    miner_command = f"xmrig -o pool.minexmr.com:443 -u {wallet} --tls" if mining_algorithm == "monero" else f"t-rex -a ethash -o stratum+tcp://eu1.ethermine.org:4444 -u {wallet}"
    subprocess.Popen(miner_command, shell=True)

if __name__ == "__main__":
    wallet_address = os.getenv("WALLET_ADDRESS", "YOUR_WALLET_ADDRESS")
    start_mining(wallet_address)
