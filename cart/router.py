from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

import db
from auth.jwt import get_current_user
from user.schema import User
from cart import services, schema

router = APIRouter(tags=["Cart"], prefix="/cart")


@router.get("/add", status_code=status.HTTP_201_CREATED)
async def add_product_to_cart(
    product_id: int,
    database: Session = Depends(db.get_db),
    current_user: User = Depends(get_current_user),
):
    result = await services.add_to_cart(product_id, current_user, database)
    return result


@router.get("/", response_model=schema.ShowCart)
async def get_all_art_items(
    database: Session = Depends(db.get_db),
    current_user: User = Depends(get_current_user),
):
    result = await services.get_all_items(current_user, database)
    return result


@router.delete("/{cart_itemid}", status_code=status.HTTP_204_NO_CONTENT)
async def remove_cart_item_by_id(
    cart_item_id: int,
    database: Session = Depends(db.get_db),
    current_user: User = Depends(get_current_user),
):
    await services.remove_cart_item(cart_item_id, current_user, database)
