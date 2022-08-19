import os

import pytest

from user.models import User


@pytest.fixture(autouse=True)
def create_dummy_user(tmpdir):
    from tests.integration.conf_test_db import override_get_db

    os.environ["NAME"] = "John"
    os.environ["EMAIL"] = "john@gmail.co"
    os.environ["PASSWORD"] = "john123"
    database = next(override_get_db())
    new_user = User(
        name=os.getenv("NAME"), email=os.getenv("EMAIL"), password=os.getenv("PASSWORD")
    )
    database.add(new_user)
    database.commit()

    yield

    database.query(User).filter(User.email == os.getenv("EMAIL")).delete()
    database.commit()
