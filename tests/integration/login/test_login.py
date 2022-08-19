import os

import pytest
from httpx import AsyncClient

from tests.integration.conf_test_db import app


@pytest.mark.asyncio
async def test_login():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post(
            "/login",
            data={"username": os.getenv("EMAIL"), "password": os.getenv("PASSWORD")},
        )
    assert response.status_code == 200
