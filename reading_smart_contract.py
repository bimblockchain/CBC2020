#imports web3.py, then sets indura project node
from web3 import Web3
infura_url = "https://mainnet.infura.io/v3/029c7ec526724b59b345469899f0dd9e"
web3 = Web3(Web3.HTTPProvider(infura_url))

#communicate that we have a connection with the blockchain
print(web3.isConnected())

#print the current blockNumber
print(web3.eth.blockNumber)

#retrieve the balance from an account
balance = web3.eth.getBalance("PLACE THE ACCOUNT ADDRESS HERE")

#print the balance with Ether
print(web3.fromWei(balance, 'ether'))
