from flask import jsonify, request
import json
import hashlib
from uuid import uuid4

from blockchain import blockchain

blockchain = blockchain()

node_address = str(uuid4()).replace('-','')

def add_transaction(sender, receiver, amount):
    index = blockchain.add_transaction(sender, receiver, amount)
    response = {'message': f'This transaction is added successfully to the block {index}'}
    return response

def get_chain():
    response = {
        'chain' : blockchain.chain,
        'length' : len(blockchain.chain)
    }
    return response