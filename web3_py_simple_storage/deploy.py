from solcx import compile_standard
import json
import time
from web3 import Web3
import os

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
    solc_version="0.8.7"
)

# print(compiled_sol)
print("\nCode successfully compiled!\n")

# Dump file creation (json with low level code)
with open("compiled_code.json", "w") as file:
    json.dump(compiled_sol, file)

print("A json with the compiled code is available in the same directory\nLook for: \"compiled_code.json\"")


# get bytecode
bytecode = compiled_sol["contracts"]["SimpleStorage"]["SimpleStorage"]["evm"]["bytecode"]["object"]

# get abi
abi = compiled_sol["contracts"]["SimpleStorage"]["SimpleStorage"]["abi"]

# print(bytecode)
# print(abi)

# for connecting to Ganache 

w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))
chain_id =  1337
my_address = "0xf07cf888a01689146a2A4f831eCD94B5AAb00600"
private_key = "0x4908e036ad16a2721762089202f99fc18699bd532734217eef0c1f52e1c99163"

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
    {"chainId":chain_id, "from": my_address, "nonce": nonce }
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
simple_storage = w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)
print(f"Initial Stored Value {simple_storage.functions.retrieve().call()}")
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