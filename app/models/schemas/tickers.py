from pydantic import BaseModel


class TickerInList(BaseModel):
    tickers: dict
    #news: dict
