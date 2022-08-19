from celery import Celery
from fastapi import FastAPI
from user import router as user_router
from products import router as product_router
from cart import router as cart_router
from orders import router as orders_router
from auth import router as auth_router

app = FastAPI(title="EcommerceApp", version="0.0.1")

app.include_router(auth_router.router)
app.include_router(user_router.router)
app.include_router(product_router.router)
app.include_router(cart_router.router)
app.include_router(orders_router.router)

celery = Celery(
    __name__, broker=f"amqp://localhost", backend=f"db+sqlite:///celery.sqlite"
)

celery.conf.imports = ["orders.tasks"]
