from brownie import accounts, SimpleStorage


def deploy_simple_storage():
    account = accounts[0]
    SimpleStorage.deploy({'from': account})


def main():
    deploy_simple_storage()