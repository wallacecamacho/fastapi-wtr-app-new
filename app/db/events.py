from app.core.settings.app import AppSettings
from fastapi import FastAPI
from loguru import logger


async def connect_to_db(app: FastAPI, settings: AppSettings):
    logger.info('Connecting to a database')

    # app.state.pool = await asyncpg.create_pool(
    #    str(settings.database_url),
    #    min_size=settings.min_connection_count,
    #    max_size=settings.max_connection_count,
    # )

    logger.info('Connection established')


async def close_db_connection(app: FastAPI) -> None:
    logger.info('Closing connection to a database')

    # await app.state.pool.close()

    logger.info('Connection closed')
