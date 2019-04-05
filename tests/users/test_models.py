import datetime

import pytest

from tests.models_factory import UserFactory, SendbackAccountFactory, PayableFactory 
from tests.models_factory import PendingTransactionFactory, SendbackTransactionFactory
from app.users.models import Log


def test_create_user(db_session):
    user = UserFactory()

    db_session.add(user)
    db_session.commit()

    users = User.query.all()
    assert len(users) == 1
    assert user == list(users)[0]

def test_create_sendbackaccount(db_session):
    sba = SendbackAccountFactory()

    db_session.add(sba)
    db_session.commit()

    sbas = SendbackAccount.query.all()
    assert len(sbas) == 1
    assert sba == list(sbas)[0]

def test_create_sendbacktransactions(db_session):
    sbt = SendbackTransactionFactory()

    db_session.add(sbt)
    db_session.commit()

    sbts = SendbackTransaction.query.all()
    assert len(sbts) == 1
    assert sbt == list(sbts)[0]

def test_create_payables(db_session):
    payable = PayableFactory()

    db_session.add(payable)
    db_session.commit()

    payables = Payable.query.all()
    assert len(payables) == 1
    assert payable == list(payables)[0]

def test_create_pending_transactions(db_session):
    ptx = PendingTransactionFactory()

    db_session.add(ptx)
    db_session.commit()

    ptxs = PendingTransaction.query.all()
    assert len(ptxs) == 1
    assert ptx == list(ptxs)[0]
