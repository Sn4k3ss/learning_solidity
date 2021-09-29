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


def interact_with_contract():
    contract.store(15, {"from": account})
    print(contract.retrieve())


def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        accounts.add(config["wallets"]["from_key"])


def main():
    deploy_simple_storage()

    interact_with_contract()