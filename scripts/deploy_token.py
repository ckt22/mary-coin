from scripts.helpful_scripts import get_account_v2
from brownie import MaryToken
from web3 import Web3

initial_supply = Web3.toWei(100000, "ether")

def main():
    account = get_account_v2()
    mary_token = MaryToken.deploy(initial_supply, {"from": account}, publish_source=True)
