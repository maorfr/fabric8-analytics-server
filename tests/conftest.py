"""Definition of fixtures for static data, sessions etc. used by unit tests."""

import os

from flask import current_app
import pytest

from f8a_worker.models import Base
from bayesian import create_app


@pytest.fixture
def someuser(rdb):
    """Fixture with one record with user data."""
    user = current_app.user_datastore.create_user(login='someuser', id=1)
    rdb.session.commit()
    return user


@pytest.fixture
def auth_header(rdb, someuser):
    """Fixture with authorization header."""
    return ('Authorization', 'token ' + someuser.generate_auth_token()[0])


@pytest.fixture
def app():
    """Fixture with an application context."""
    here = os.path.dirname(__file__)
    app = create_app(configfile=os.path.join(here, 'appconfig.py'))
    return app


@pytest.fixture
def rdb(app, request):
    """Fixture with static data in RDB."""
    # TODO: we may need to run actual migrations here
    app.rdb.drop_all()
    Base.metadata.drop_all(bind=app.rdb.engine)

    Base.metadata.create_all(bind=app.rdb.engine)
    app.rdb.create_all()
    return app.rdb
