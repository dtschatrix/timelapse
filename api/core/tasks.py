from fastapi import FastAPI
from databases import Database
from database import database_url
import logging


logger = logging.getLogger(__name__)


async def connect_to_db(app: FastAPI) -> None:
    database = Database(database_url, min_size=2, max_size=10)
    try:
        await database.connect()
        app.state._db = database
    except Exception as e:
        logger.warn("--- DB CONNECTION ERROR ---")
        logger.warn(e)


async def close_db_connection(app: FastAPI) -> None:
    try:
        await app.state._db.disconnect()
    except Exception as e:
        logger.warn("--- DB DISCONNECT ERROR ---")
        logger.warn(e)