
import json
from web3 import Web3

#change to a testnet.
#mainnet infura_url = "https://mainnet.infura.io/v3/029c7ec526724b59b345469899f0dd9e"
infura_url = "https://ropsten.infura.io/v3/029c7ec526724b59b345469899f0dd9e" #ropsten testnetwork - check the infura projec dbim on how it is set
web3 = Web3(Web3.HTTPProvider(infura_url))

#communicate that we have a connection with the blockchain
print(web3.isConnected())


#be careful with the private key, never publish the contract as such.
account_A = "insert ETH Address here"
key = "insertprivatekey here"

#execution fails throwing the following error: "TypeError: Transaction had invalid fields: {'to': '0x7e01cf301c0f55f0a50100d67ca16accd75ae1d8'}
#which probably means we somehow have to declare in another manner the receiving account?
#account_W = "0x7e01cf301c0f55f0a50100d67ca16accd75ae1d8"


#get the nonce
nonce = web3.eth.getTransactionCount(account_A)
#build a transaction
tx = {
    'nonce': nonce,
    'to': 'insert the address you want to send to here.', #be careful with typing / copying addresses
    'value': web3.toWei(0.042, 'ether'),
    'gas': 210000,
    'gasPrice': web3.toWei('50', 'gwei'),
    'chainId': 1
}
#sign the transaction
signed_tx = web3.eth.account.sign_transaction(tx, key)
signed_tx.rawTransaction #you 

# send the transaction
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)


# get transaction hash
print(tx_hash)
