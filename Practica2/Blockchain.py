from hashlib import sha256
import json
from time import time

class Block():
    def __init__(self, index, transactions, timestamp, previous_hash, _nonce = 0) -> None:
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = _nonce
    
    def compute_hash(self):
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return sha256(block_string.encode()).hexdigest()

    def __str__(self) -> str:
        return str({
            "index": self.index,
            "transactions": self.transactions,
            "timestamp": self.timestamp,
            "previous_hash": self.previous_hash,
            "hash": self.hash,
            "nonce": self.nonce
        })


class Blockchain():
    __difficulty = 2

    def __init__(self) -> None:
        self.chain = []
        self.unconfirmed_transactions = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(0, [], time(), '0')
        genesis_block.hash = self.proof_of_work(genesis_block)
        self.chain.append(genesis_block)

    @property
    def last_block(self):
        return self.chain[-1]
    
    def is_valid_proof(self, block, block_hash) -> bool:
        verification = (block_hash.startswith('0'*self.__difficulty)
                        and block_hash == block.compute_hash())
        return verification
    

    def add_block(self, block, proof) -> bool:
        
        previous_hash = self.last_block.hash

        if previous_hash != block.previous_hash:
            return False

        if not self.is_valid_proof(block, proof):
            return False

        block.hash = proof
        self.chain.append(block)
        return True

    def add_new_transaction(self, transaction):
        self.unconfirmed_transactions.append(transaction)


    def mine(self):

        if len(self.unconfirmed_transactions) == 0:
            return False

        last_block = self.last_block

        new_block = Block(index=last_block.index+1,
                          transactions=self.unconfirmed_transactions,
                          timestamp=time(),
                          previous_hash=last_block.hash)

        print("Minando.....")
        proof = self.proof_of_work(new_block)

        print("previous_hash:", last_block.hash)
        print("proof:", proof)

        is_valid = self.add_block(block=new_block, proof=proof)

        if not is_valid:
            print("Bloque no fue agregado")
            return False

        print("Bloque agregado con exito.")
        self.unconfirmed_transactions = []
        return True


    def check_chain_validity(self, chain):
        result = True
        previous_hash = '0'

        # Iterar bloques a traves de toda la cadena de bloques
        for block in chain:
            block_hash = block.hash

            # Eliminar el campo hash para volver a calcular el hash nuevamente
            block.hash = ""

            if not self.is_valid_proof(block, block_hash) or previous_hash != block.previous_hash:
                result = False
                break

            block.hash, previous_hash = block_hash, block_hash

        return result


# Nodo 1
blockchain1 = Blockchain()
# Bloque Genesis:
genesis_block = blockchain1.last_block
print("Genesis Block:", genesis_block)
print("========================= Genesis Block ======================")

# Agregar transacciones no confirmadas - Primer proceso
# Estructura de la transaccion => {"wallet": int, "amount": float}
blockchain1.add_new_transaction({"wallet": 1, "amount": 100})
blockchain1.add_new_transaction({"wallet": 1, "amount": 50})
blockchain1.add_new_transaction({"wallet": 2, "amount": 40})
blockchain1.add_new_transaction({"wallet": 3, "amount": 10})
