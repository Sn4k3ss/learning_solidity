from brownie import PoliToken, accounts, network, config
from my_token.scripts.helpful_scripts import *


def main():
    account = get_account(index=0)
    PoliToken.deploy(1e21, {"from": account})
