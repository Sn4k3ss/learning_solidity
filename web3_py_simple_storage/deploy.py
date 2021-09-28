from solcx import compile_standard
import json
import time
from web3 import Web3
import os
from dotenv import load_dotenv

# printing what's inside of "SimpleStorage.sol"
with open("./SimpleStorage.sol", "r") as file:
    simple_storage_file = file.read()
    # print(simple_storage_file)


# compiling smart contract with solcx
print("\n-----------  Compiling  -----------")
time.sleep(0.2)
print("...")
time.sleep(0.2)
print("...")
time.sleep(0.2)
print("...")


compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"SimpleStorage": {"content": simple_storage_file}},
        "settings": {
            "outputSelection": {
                "*": {"*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]}
            }
        },
    },
    solc_version="0.8.7",
)

# print(compiled_sol)
print("\nCode successfully compiled!\n")

# Dump file creation (json with low level code)
with open("compiled_code.json", "w") as file:
    json.dump(compiled_sol, file)

print(
    'A json with the compiled code is available in the same directory\nLook for: "compiled_code.json"'
)


# get bytecode
bytecode = compiled_sol["contracts"]["SimpleStorage"]["SimpleStorage"]["evm"][
    "bytecode"
]["object"]

# get abi
abi = compiled_sol["contracts"]["SimpleStorage"]["SimpleStorage"]["abi"]

# print(bytecode)
# print(abi)

# for connecting to Ganache

w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:8545"))
chain_id = 1337
my_address = "0x90F8bf6A479f320ead074411a4B0e7944Ea8c9C1"
load_dotenv()
private_key = os.getenv('PRIVATE_KEY')

# create the contract in python
SimpleStorage = w3.eth.contract(abi=abi, bytecode=bytecode)

# get latest transaction (nounce)
nonce = w3.eth.getTransactionCount(my_address)
# print(nonce)

# 1. Build a txn
# 2. Sign the txn
# 3. Send the txn

# 1
transaction = SimpleStorage.constructor().buildTransaction(
    {"chainId": chain_id, "from": my_address, "nonce": nonce}
)

# 2 Sign
signed_txn = w3.eth.account.sign_transaction(transaction, private_key=private_key)


# 3 Send it!
tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)

# Wait for the transaction to be mined, and get the transaction receipt
print("Waiting for transaction to finish...")
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print(f"Done! Contract deployed to {tx_receipt.contractAddress}")

# Working with deployed Contracts
#
# To work with Contracts you need:
# Contract ABI => You can get the abi from google
# Contract Address => from the receipt if you are the one deployng the contract
simple_storage = w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)


# 'call' -> Simulate making the transaction and get the return value
# 'transaction' -> Actually make a state change of the blockchain

# Calling function retrieve (NO STATE CHANGE)
print(f"Initial Stored Value {simple_storage.functions.retrieve().call()}")

# Executing a transaction (CHANGE BLOCKCHAIN STATE)
greeting_transaction = simple_storage.functions.store(15).buildTransaction(
    {"chainId": chain_id, "from": my_address, "nonce": nonce + 1}
)


signed_greeting_txn = w3.eth.account.sign_transaction(
    greeting_transaction, private_key=private_key
)


tx_greeting_hash = w3.eth.send_raw_transaction(signed_greeting_txn.rawTransaction)

print("Updating stored Value...")

tx_receipt = w3.eth.wait_for_transaction_receipt(tx_greeting_hash)

print(simple_storage.functions.retrieve().call())
