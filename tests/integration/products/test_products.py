import pytest
from httpx import AsyncClient

from tests.integration.conf_test_db import app
from tests.integration.shared.info import category_info, product_info


@pytest.mark.asyncio
async def test_new_prodcut():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        category_obj = await category_info()
        payload = {
            "name": "Quaker Oats",
            "quantity": 4,
            "description": "Quaker: Good Quality Oats",
            "price": 10,
            "category_id": category_obj.id,
        }

        response = await ac.post("/products/", json=payload)
    assert response.status_code == 201
    assert response.json()["name"] == "Quaker Oats"
    assert response.json()["quantity"] == 4
    assert response.json()["description"] == "Quaker: Good Quality Oats"
    assert response.json()["price"] == 10


@pytest.mark.asyncio
async def test_list_products():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        category_obj = await category_info()
        await product_info(category_obj)
        response = await ac.get("/products/")
    assert response.status_code == 200
    assert "name" in response.json()[0]
    assert "quantity" in response.json()[0]
    assert "description" in response.json()[0]
    assert "price" in response.json()[0]
