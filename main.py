"""Əsas servislər UserService və OrderService monolitik architekturada"""

from fastapi import FastAPI

from database import connection
from order import Order
from user import User

app = FastAPI()


async def create_connection():
    try:
        await connection.connect()
    except Exception as e:
        print(f"Connection error: {e}")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8001)
