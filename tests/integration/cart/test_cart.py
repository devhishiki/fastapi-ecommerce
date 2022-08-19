import os

import pytest
from httpx import AsyncClient

from auth.jwt import create_access_token
from user.models import User
from tests.integration.conf_test_db import app
from tests.integration.shared.info import product_info, category_info


@pytest.mark.asyncio
async def test_add_to_cart():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        category_obj = await category_info()
        product_obj = await product_info(category_obj)
        user = User(
            name=os.getenv("NAME"),
            email=os.getenv("EMAIL"),
            password=os.getenv("PASSWORD"),
        )
        user_access_token = create_access_token(user)

        response = await ac.get(
            "/cart/add",
            params={"product_id": product_obj.id},
            headers={"Authorization": f"Bearer {user_access_token}"},
        )
    assert response.status_code == 201
    assert response.json() == {"status": "Item Added to Cart"}


@pytest.mark.asyncio
async def test_cart_listing():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        user = User(
            name=os.getenv("NAME"),
            email=os.getenv("EMAIL"),
            password=os.getenv("PASSWORD"),
        )
        user_access_token = create_access_token(user)
        response = await ac.get(
            "/cart/", headers={"Authorization": f"Bearer {user_access_token}"}
        )
    assert response.status_code == 200
