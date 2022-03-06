#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 11:50:24 2022

@author: oscar
"""
#%% init
from web3 import Web3

ganache_url = 'http://127.0.0.1:7545'

web3 = Web3(Web3.HTTPProvider(ganache_url))
print(f'Connnected ganache: {web3.isConnected()}')
print(f'Block connected: {web3.eth.blockNumber}')

account_1 ='0x795dbf05bC49f8B96E7A49075eb5e673E30E367C'
account_2 = '0xC956654BD934d456f1C473fd2D7aD8598Fd1d1a0'

private_key = '91707f44eaff6a83eda315fd4f9262903db5139bc0d64b58a843ff3c0dfee336'

#%% get the nonce
nonce = web3.eth.getTransactionCount(account_1)

#%% build transaction
tx = {
      'nonce': nonce,
      'to': account_2,
      'value': web3.toWei(1, 'ether'),
      'gas': 2000000,
      'gasPrice': web3.toWei('50', 'gwei')
      }

#%% sign transaction
signed_tx = web3.eth.account.signTransaction(tx, private_key)

#%% send transaction
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)

#%% get transaction hash
print(f'Transsaction hash: {web3.toHex(tx_hash)}')