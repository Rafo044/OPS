"""Database-lə baglı əlaqələr bu modulda olacaq"""

import os

from dotenv import load_dotenv
from loguru import logger
from psycopg2 import connect

load_dotenv()


def connection():
    try:
        connection_ = connect(
            host=os.getenv("HOST"),
            database=os.getenv("POSTGRES_DATABASE"),
            user=os.getenv("POSTGRES_USER"),
            password=os.getenv("POSTGRES_PASSWORD"),
            port=os.getenv("POSTGRES_PORT"),
        )
        return connection_
        logger.success("Connected to the database")
    except Exception as e:
        logger.error(f"Error connecting to the database: {e}")
        return e


connection()
