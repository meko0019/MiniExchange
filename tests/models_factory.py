import datetime

import factory.fuzzy

from app.users.models import *

class BaseModelFactory(factory.Factory):
    class Meta:
        abstract = True


class UserFactory(BaseModelFactory):
    class Meta:
        model = User

    username = factory.fuzzy.FuzzyText(length=8)
    email = factory.fuzzy.FuzzyText(length=8)


class SendbackAccountFactory(BaseModelFactory):
    class Meta:
        model = SendbackAccount

    stellar_name = factory.fuzzy.FuzzyText(length=8)
    address = factory.fuzzy.FuzzyText(length=8)
    destination_tag = factory.fuzzy.FuzzyInteger(length=8)
 

class SendbackTransactionFactory(BaseModel):
    class Meta:
        model = SendbackTransaction

    account_sender = factory.fuzzy.FuzzyText(length=8)
    amount_sender = factory.fuzzy.FuzzyInteger(length=8)
    destination_sender = factory.fuzzy.FuzzyText(length=8)
    destination_tag_sender = factory.fuzzy.FuzzyInteger(length=8)
    fee_sender = factory.fuzzy.FuzzyInteger(length=8)
    flags_sender = factory.fuzzy.FuzzyText(length=8)
    sequence_sender = factory.fuzzy.FuzzyText(length=8)
    signing_pub_key_sender = factory.fuzzy.FuzzyText(length=8)
    transaction_type_sender = factory.fuzzy.FuzzyText(length=8)
    tx_signature_sender = factory.fuzzy.FuzzyText(length=8)
    tx_hash_sender = factory.fuzzy.FuzzyText(length=8)
    ledger_index_sender = factory.fuzzy.FuzzyText(length=8)
    date_sender = factory.fuzzy.FuzzyText(length=8)
    ledger_hash_sender = factory.fuzzy.FuzzyText(length=8)
    validated_sender = False


class PayableFactory(BaseModel):
    class Meta:
        model = Payable

    destination = factory.fuzzy.FuzzyText(length=8)
    amount = factory.fuzzy.FuzzyInteger(length=8)
    tx_signed = False
    tx_submitted = False
    tx_validated = False

    tx_blob = factory.fuzzy.FuzzyText(length=8)
    tx_hash = factory.fuzzy.FuzzyText(length=8)

    account_fulfilled = factory.fuzzy.FuzzyText(length=8)
    amount_fulfilled = factory.fuzzy.FuzzyInteger(length=8)
    destination_fulfilled = factory.fuzzy.FuzzyText(length=8)
    destination_tag_fulfilled = factory.fuzzy.FuzzyInteger(length=8)
    fee_fulfilled = factory.fuzzy.FuzzyInteger(length=8)
    flags_fulfilled = factory.fuzzy.FuzzyText(length=8)
    sequence_fulfilled = factory.fuzzy.FuzzyText(length=8)
    signing_pub_key_fulfilled = factory.fuzzy.FuzzyText(length=8)
    transaction_type_fulfilled = factory.fuzzy.FuzzyText(length=8)
    tx_signature_fulfilled = factory.fuzzy.FuzzyText(length=8)
    tx_hash_fulfilled = factory.fuzzy.FuzzyText(length=8)
    date_fulfilled = factory.fuzzy.FuzzyText(length=8)
    ledger_hash_fulfilled = factory.fuzzy.FuzzyText(length=8)
    ledger_index_fulfilled = factory.fuzzy.FuzzyText(length=8)


class PendingTransactionFactory(BaseModel):
    class Meta:
        model = PendingTransaction

    destination = factory.fuzzy.FuzzyText(length=8)
    amount = factory.fuzzy.FuzzyInteger(length=8)
    tx_signed = False
    tx_submitted = False
    tx_validated = False
    sequence = factory.fuzzy.FuzzyInteger(length=8)

    tx_blob = factory.fuzzy.FuzzyText(length=8)
    tx_hash = factory.fuzzy.FuzzyText(length=8)










