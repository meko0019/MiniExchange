import os
import shutil
import tempfile

import pytest

from app import database
from app.database.utils import delete_all_rows
from app.factory import create_app


@pytest.yield_fixture(scope="session")
def tmp():
    tmpdir = tempfile.mkdtemp(prefix="pytest-app-", dir="/tmp")
    yield tmpdir
    try:
        shutil.rmtree(tmpdir)
    except Exception:
        pass


@pytest.fixture(scope="session")
def app(tmp):
    return create_app()


@pytest.fixture(scope="session")
def db(app):
    database.db.app = app
    delete_all_rows(app)
    return database.db


@pytest.fixture(scope="function")
def db_session(db, request):
    connection = db.engine.connect()
    transaction = connection.begin()

    options = dict(bind=connection, binds={})
    session = db.create_scoped_session(options=options)
    db.session = session

    def teardown():
        transaction.rollback()
        connection.close()
        session.remove()

    request.addfinalizer(teardown)
    return session