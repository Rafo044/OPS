"""Database-lə baglı əlaqələr bu modulda olacaq"""

import os

from dotenv import load_dotenv
from loguru import logger
from tortoise import Tortoise

load_dotenv()


async def connection():
    try:
        await Tortoise.init(
            db_url=f"postgres://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@{os.getenv('POSTGRES_HOST')}:{os.getenv('POSTGRES_PORT')}/{os.getenv('POSTGRES_DB')}",
            modules={"models": ["user"]},
        )
        await Tortoise.generate_schemas()
        logger.info("Baglantı ugurla reallaşdı!")
    except Exception as e:
        logger.error(f"Baglantı zamanı xəta baş verdi: {e}")
        raise


async def close_db():
    await Tortoise.close_connections()
