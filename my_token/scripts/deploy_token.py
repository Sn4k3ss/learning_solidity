from brownie import PoliToken, Token, accounts, network, config
from scripts.helpful_scripts import *


def deply_token():
    account = get_account()

    PoliToken.deploy(1e21, {"from": account})
    #  Token.deploy("PoliToken", "POLI", 8, 1e11, {"from": account})


def verify_token():
    token = PoliToken[-1]
    PoliToken.publish_source(token)


def main():
    deply_token()
    verify_token()
