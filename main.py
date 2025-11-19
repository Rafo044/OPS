"""Əsas servislər UserService və OrderService monolitik architekturada"""

from fastapi import FastAPI
from loguru import logger

from database import connection
from order import Order
from user import User

logger.add("main.log", rotation="10 MB", retention="10 days")

app = FastAPI()


async def create_connection():
    try:
        return connection
    except Exception as e:
        logger.error(f"Connection error: {e}")


@app.get("/connection")
async def get_connection():
    connection_response = await create_connection()
    return connection_response


@app.get("/user")
async def get_user():
    user = User()
    return user


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8001)
