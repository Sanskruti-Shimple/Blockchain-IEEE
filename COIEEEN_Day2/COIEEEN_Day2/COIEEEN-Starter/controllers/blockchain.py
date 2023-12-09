from flask import jsonify, request
import json
import hashlib
from uuid import uuid4

from blockchain import Blockchain

blockchain = Blockchain()

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

def mine_block():
    previous_block = blockchain.get_previous_block()
    previous_proof= previous_block['proof']

    proof=blockchain.proof_of_work(previous_proof)
    previous_hash = previous_block['block_hash']
    block_hash = hashlib.sha256(str(proof**2 - previous_proof**2).encode()).hexdigest()

    blockchain.add_transaction(sender=node_address, receiver='You',amount=1)
    block=blockchain.create_block(proof,previous_hash,block_hash)
    response= {'message': "congratulations, you you just mined a block!",
               'index':block['index'],
                'timestamp':block['timestamp'],
                'proof':block['proof'],
                'previous_hash': block['previous_hash'],
                'block_hash': block['block_hash'],
                'transactions': block['transactions']
    }
    return response

def is_valid():
    is_valid=blockchain.is_chain_valid(blockchain.chain)
    return is_valid
