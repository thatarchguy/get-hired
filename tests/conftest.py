import pytest
from hired import app, db, models

app.config.from_object('config.TestConfig')


def initialize():
    db.create_all()
    db.session.commit()


# Create a fresh database
initialize()


@pytest.fixture(scope='module')
def client():
    client = app.test_client()
    return client
