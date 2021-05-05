import time
import json
import hashlib as h

# class Block:
#     def __init__(self, index, transactions, timestamp, prevhash):
#         self.index = index
#         self.transactions = transactions
#         self.timestamp = timestamp
#         self.prevhash = prevhash
#         self.nonce = 0
#
#
#
#     """
#     Hashes are used to verify a transaction has never occurred
#     - Eg. a transaction occurs - you has it
#         - a second transaction occurs, you has and then compare with other hashes to note that this hasnt happened before
#         - this stores the data forever - and hashes can be looked up quickly
#     """
#
#     def compute_hash(self):
#         block_string = json.dumps(self.__dict__, sort_keys=True)
#         return h.sha256(block_string.encode()).hexdigest()


"""
To ensure immutability: include a hash of the previous block within the current block
- the awareness of all data establishes a mechanism for protecting the entire chains integrity
"""


class Blockchain:
    def __init__(self):
        self.unconfirmed_transactions = []
        self.chain = {}
        self.chain[0] = self.create_genesis_block()
        self._save_json()

    def create_block(self, transactions, timestamp, prevhash):
        dict = {}
        dict['transactions'] = transactions
        dict['timestamp'] = timestamp
        dict['prevhash'] = prevhash
        dict['nonce'] = 0
        return dict

    def compute_hash(self, dict):
        block_string = json.dumps(dict, sort_keys=True)
        return h.sha256(block_string.encode()).hexdigest()

    def create_genesis_block(self):
        genesis_block = self.create_block([], time.time(), "0")
        genesis_block['hash'] = self.compute_hash(genesis_block)
        return genesis_block

    @property
    def prev_block(self):
        index = list(self.chain.keys())[-1]
        return self.chain[index]

    """
    Now we must ensure noone can manipulate previous blocks and recompute each of the following blocks
    
    We must also implement a way for users to come to a consensus on a single chronological history of the chain
    - initial consensus method was proof of work (btc)
    
    Proof of work:
    - makes it progressively harder to perform the work required to create a new block (and all following blocks)
    - requires scanning for a value that starts with a certain number of zero bits when hashed = NONCE VALUE
    - # of leading zeros is the difficulty
    - this makes it nearly impossible to manipulate a block and all following blocks in time to catch up
    """

    difficulty = 2

    def proof_of_work(self, block):
        block['nonce'] = 0
        computed_hash = self.compute_hash(block)
        block['hash'] = computed_hash
        while not computed_hash.startswith('0' * Blockchain.difficulty):
            block['nonce'] += 1
            computed_hash = self.compute_hash(block)
            # block['hash'] = computed_hash
        return computed_hash

    """
    Initially transactions are stored in unconfirmed_transactions
    - once confirmed as a valid proof that satisfies the difficulty criteria, we add it to the chain
    - this process of performing the computational work of validating is "mining"
    """

    def add_block(self, block, proof):
        previous_hash = self.prev_block['hash']

        if previous_hash != block['prevhash']:
            return False

        if not self.is_valid_proof(block, proof):
            return False

        block['hash'] = proof
        index = list(self.chain.keys())[-1]
        self.chain[index + 1] = block
        return True

    def is_valid_proof(self, block, block_hash):
        return (block_hash.startswith('0' * Blockchain.difficulty) and
                block_hash == self.compute_hash(block))

    def add_new_transaction(self, transaction):
        self.unconfirmed_transactions.append(transaction)

    def mine(self):
        if not self.unconfirmed_transactions:
            return False

        last_block = self.prev_block
        new_block = self.create_block(transactions=self.unconfirmed_transactions,
                                      timestamp=time.time(),
                                      prevhash=last_block['hash'])

        proof = self.proof_of_work(new_block)
        self.add_block(new_block, proof)
        self.unconfirmed_transactions = []

        self._save_json()
        return list(self.chain.keys())[-1]

    def _save_json(self):
        with open('blockchain.json', 'w') as f:
            json.dump(self.chain, f, indent=2)
