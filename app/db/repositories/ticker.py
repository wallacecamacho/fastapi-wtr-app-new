from typing import Any

from app.core.utils.stocks import Stocks
from app.db.errors import StocksYFinanceException
from loguru import logger


class TickerRepository:
    def __init__(self) -> None:
        self = self

    async def get_tickers(self, ticker: str, start: str, end: str) -> Any:

        try:
            stock = Stocks(ticker, start=start, end=end)
            stock_return = {
                #'news': stock.news,
                'tickers': stock.tickers
            }
            return stock_return
        except ValueError as ve:
            logger.error('Error' + str(ve))
        except StocksYFinanceException as e:
            logger.error('StocksYFinanceException error' + str(e))
