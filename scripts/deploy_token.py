from scripts.helpful_scripts import get_account_v2
from brownie import MaryCoin
from web3 import Web3

initial_supply = Web3.toWei(1000, "ether")

def main():
    account = get_account_v2()
    mary_coin = MaryCoin.deploy(initial_supply, {"from": account}, publish_source=True)
