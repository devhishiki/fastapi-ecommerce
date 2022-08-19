import os

APP_ENV = os.getenv("APP_ENV", "development")
DATABASE_USERNAME = os.getenv("DATABASE_USERNAME", "postgres")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD", "postgres")
DATABASE_HOST = os.getenv("DATABASE_HOST", "localhost")
DATABASE_NAME = os.getenv("DATABASE_NAME", "ecommerce")
CELERY_BROKER_URL = "amqp://localhost"
# CELERY_BROKER_URL = 'amqp://192.168.64.4:30672'
CELERY_RESULT_BACKEND = "db+sqlite:///results.sqlite"

TEST_DATABASE_NAME = os.getenv("TEST_DATABASE_NAME", "ecommerce_test")
