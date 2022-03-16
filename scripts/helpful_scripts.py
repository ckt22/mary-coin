from brownie import (
    accounts,
    config,
    network,
)
from web3 import Web3

DECIMALS=8
STARTING_VALUE=200000000000
LOCAL_BLOCKCHAIN_ENVIRONMENTS=["development", "ganache-local"]
FORKED_LOCAL_ENVIRONMENTS=["mainnet-fork-dev"]

def get_account():
    if (network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS 
    or network.show_active() in FORKED_LOCAL_ENVIRONMENTS):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

def get_account_v2(index=None, id=None):
    if (index):
        return accounts[index]
    if (id):
        return accounts.load(id)
    if (network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS 
    or network.show_active() in FORKED_LOCAL_ENVIRONMENTS):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

# def fund_with_link(
#     contract_address, account=None, link_token=None, amount=2000000000000000000
# ):  # 2 LINK
#     account = account if account else get_account()
#     link_token = link_token if link_token else get_contract("link_token")
#     tx = link_token.transfer(contract_address, amount, {"from": account})
#     # link_token_contract = interface.LinkTokenInterface(link_token.address)
#     # tx = link_token_contract.transfer(contract_address, amount, {"from": account})
#     tx.wait(1)
#     print("Fund contract!")
#     return tx