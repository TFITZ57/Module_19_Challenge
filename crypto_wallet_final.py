import os
from web3 import Web3
from eth_account import Account
from dotenv import load_dotenv
from bip44 import Wallet
from mnemonic import Mnemonic

# Load environment variables
load_dotenv('SAMPLE.env')

# Fetch mnemonic from .env
mnemonic = os.getenv("MNEMONIC")
provider_uri = os.getenv("WEB3_PROVIDER_URI")

# Initialize Web3
w3 = Web3(Web3.HTTPProvider(provider_uri))

def generate_account():
    if not mnemonic:
        raise ValueError("Mnemonic not found in environment variables")
    
    # Initialize wallet with the mnemonic
    wallet = Wallet(mnemonic)
    
    # Derive the private key for the first account
    private_key, public_key = wallet.derive_account("eth", 0)
    
    # Create an account object from the private key
    account = Account.from_key(private_key)
    
    return account

def get_balance(w3, address):
    balance = w3.eth.get_balance(address)
    return Web3.from_wei(balance, 'ether')

def send_transaction(w3, account, to, wage):
    tx = {
        'nonce': w3.eth.get_transaction_count(account.address),
        'to': to,
        'value': Web3.to_wei(wage, 'ether'),
        'gas': 2000000,
        'gasPrice': Web3.to_wei('50', 'gwei')
    }
    signed_tx = account.sign_transaction(tx)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    return tx_hash.hex()