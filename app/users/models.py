from app import db, BaseModel
from datetime import datetime

__all__ = ['User',
           'SendbackAccount',
           'SendbackTransaction',
           'Payable',
           'PendingTransaction'
]

class User(BaseModel):
    email = db.Column(db.String(255), unique=True)
    username = db.Column(db.String(100), unique=True)
    #TODO: add field validation, add status field with enums, etc 

    def __repr__(self):
        return f'<User: {self.email}>'

    def __json__(self):
        json = super().__json__()
        json.update({
                    'email': self.email,
                    'username': self.username,
            })


class SendbackAccount(BaseModel):
    stellar_name = db.Column(db.String(255))
    address = db.Column(db.String(255))
    destination_tag = db.Column(db.Integer)
    transactions = db.relationship('SendbackTransaction', backref='SendbackAccount', lazy='dynamic')
    payables = db.relationship('Payable', backref='SendbackAccount', lazy='dynamic')

    def __repr__(self):
        return f'<SendbackAccount: {self.stellar_name}>'

    def __json__(self):
        json = super().__json__()
        json.update({
                    'stellar_name': self.stellar_name,
                    'address': self.address,
                    'destination_tag': self.destination_tag,
                    'transactions': self.transactions.__json__(),
                    'payables': self.payables.__json__()

            })

class SendbackTransaction(BaseModel):
    sendback_account_id = db.Column(db.Integer, db.ForeignKey(SendbackAccount.id))
    account_sender = db.Column(db.String(255))
    amount_sender = db.Column(db.Integer)
    destination_sender = db.Column(db.String(255))
    destination_tag_sender = db.Column(db.Integer)
    fee_sender = db.Column(db.Integer)
    flags_sender = db.Column(db.String(255))
    sequence_sender = db.Column(db.String(255))
    signing_pub_key_sender = db.Column(db.String(255))
    transaction_type_sender = db.Column(db.String(255))
    tx_signature_sender = db.Column(db.String(255))
    tx_hash_sender = db.Column(db.String(255))
    ledger_index_sender = db.Column(db.String(255))
    date_sender = db.Column(db.String(255))
    ledger_hash_sender = db.Column(db.String(255))
    validated_sender = db.Column(db.Boolean)

    payable = db.relationship('Payable', backref='SendbackTransaction', lazy='dynamic')

    def __repr__(self):
        return f'<Transaction: {self.account} - {self.amount}>'

    def __json__(self):
        json = super().__json__()
        json.update({
                    'account_sender': self.account_sender,
                    'amount_sender': self.amount_sender,
                    'destination_sender': self.destination_sender,
                    'destination_tag_sender': self.destination_tag_sender,
                    'fee_sender': self.fee_sender,
                    'flags_sender': self.flags_sender,
                    'sequence_sender': self.sequence_sender,
                    'signing_pub_key_sender': self.signing_pub_key_sender,
                    'transaction_type_sender': self.transaction_type_sender,
                    'tx_signature_sender': self.tx_signature_sender,
                    'tx_hash_sender': self.tx_hash_sender,
                    'ledger_index_sender': self.ledger_index_sender,
                    'date_sender': self.date_sender,
                    'ledger_hash_sender': self.ledger_hash_sender,
                    'validated_sender': self.validated_sender,
                    'payable': self.payable.__json__()
            })


class Payable(BaseModel):
    destination = db.Column(db.String(255))
    amount = db.Column(db.Integer)
    sendback_transaction_id = db.Column(db.Integer, db.ForeignKey(SendbackTransaction.id))
    sendback_account_id = db.Column(db.Integer, db.ForeignKey(SendbackAccount.id))
    pending_transaction = db.relationship('PendingTransaction', backref='Payable', lazy='dynamic')
    tx_signed = db.Column(db.Boolean)
    tx_submitted = db.Column(db.Boolean)
    tx_validated = db.Column(db.Boolean)

    tx_blob = db.Column(db.String(255))
    tx_hash = db.Column(db.String(255))

    account_fulfilled = db.Column(db.String(255))
    amount_fulfilled = db.Column(db.Integer)
    destination_fulfilled = db.Column(db.String(255))
    destination_tag_fulfilled = db.Column(db.Integer)
    fee_fulfilled = db.Column(db.Integer)
    flags_fulfilled = db.Column(db.String(255))
    sequence_fulfilled = db.Column(db.String(255))
    signing_pub_key_fulfilled = db.Column(db.String(255))
    transaction_type_fulfilled = db.Column(db.String(255))
    tx_signature_fulfilled = db.Column(db.String(255))
    tx_hash_fulfilled = db.Column(db.String(255))
    date_fulfilled = db.Column(db.String(255))
    ledger_hash_fulfilled = db.Column(db.String(255))
    ledger_index_fulfilled = db.Column(db.String(255))

    def __repr__(self):
        return f'<Payable: {destination} - {amount}>'

    def __json__(self):
        json = super().__json__()
        json.update({
                    'destination': self.destination,
                    'amount': self.amount,
                    'tx_signed': self.tx_signed,
                    'tx_submitted': self.tx_submitted,
                    'tx_validated': self.tx_validated,
                    'tx_hash': self.tx_hash,
                    'tx_blob': self.tx_blob,
                    'account_fulfilled': self.account_fulfilled,
                    'amount_fulfilled': self.amount_fulfilled,
                    'destination_fulfilled': self.destination_fulfilled,
                    'destination_tag_fulfilled': self.destination_tag_fulfilled,
                    'fee_fulfilled': self.fee_fulfilled,
                    'flags_sender': self.flags_sender,
                    'sequence_fulfilled': self.sequence_fulfilled,
                    'signing_pub_key_fulfilled': self.signing_pub_key_fulfilled,
                    'transaction_type_fulfilled': self.transaction_type_fulfilled,
                    'tx_signature_fulfilled': self.tx_signature_fulfilled,
                    'tx_hash_fulfilled': self.tx_hash_fulfilled,
                    'date_fulfilled': self.date_fulfilled,
                    'ledger_hash_fulfilled': self.ledger_hash_fulfilled,
                    'ledger_index_fulfilled': self.ledger_index_fulfilled,
                    'pending_transaction': self.pending_transaction.__json__()
            })

class PendingTransaction(BaseModel):
    destination = db.Column(db.String(255))
    amount = db.Column(db.Integer)
    payable = db.Column(db.Integer, db.ForeignKey(Payable.id))
    tx_signed = db.Column(db.Boolean)
    tx_submitted = db.Column(db.Boolean)
    tx_validated = db.Column(db.Boolean)
    sequence = db.Column(db.Integer)

    tx_blob = db.Column(db.String(255))
    tx_hash = db.Column(db.String(255))

    def __repr__(self):
        return f'<Transaction: {self.destination} - {self.amount}>'


    def __json__(self):
        json = super().__json__()
        json.update({
                    'destination': self.destination,
                    'amount': self.amount,
                    'tx_signed': self.tx_signed,
                    'tx_submitted': self.tx_submitted,
                    'tx_validated': self.tx_validated,
                    'sequence': self.sequence,
                    'tx_hash': self.tx_hash,
                    'tx_blob': self.tx_blob
                    
            })










