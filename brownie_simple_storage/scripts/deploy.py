from brownie import accounts, SimpleStorage, config, network

account = ''
contract = ''

def deploy_simple_storage():
    global account, contract

    # work with local ganache account
    # account = accounts[0]

    # work with testnet/mainnet using metamask account
    # loading the addedd account
    # account = accounts.load('testing-account')
    # or load it from yaml file
    
    # account = accounts.add(config["wallets"]["from_key"])
    # contract = SimpleStorage.deploy({'from': account})

    account = get_account()
    contract = SimpleStorage.deploy({'from': account})
    stored_value = contract.retrieve()
    print(stored_value)
    transaction = contract.store(15, {"from": account})
    transaction.wait(1)
    updated_stored_value = contract.retrieve()
    print(updated_stored_value)



def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def main():
    deploy_simple_storage()