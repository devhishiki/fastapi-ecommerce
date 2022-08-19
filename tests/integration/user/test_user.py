import os

import pytest
from httpx import AsyncClient

from auth.jwt import create_access_token
from user.models import User
from tests.integration.conf_test_db import app


@pytest.mark.asyncio
async def test_all_users():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        user = User(
            name=os.getenv("NAME"),
            email=os.getenv("EMAIL"),
            password=os.getenv("PASSWORD"),
        )
        user_access_token = create_access_token(user)
        response = await ac.get(
            "/user/", headers={"Authorization": f"Bearer {user_access_token}"}
        )
    assert response.status_code == 200
