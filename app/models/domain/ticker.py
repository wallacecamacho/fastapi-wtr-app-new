from app.models.common import DateTimeModelMixin, IDModelMixin
from app.models.domain.rwmodel import RWModel


class Ticker(IDModelMixin, DateTimeModelMixin, RWModel):
    tickers: str


class TickerInDB(Ticker, IDModelMixin, DateTimeModelMixin):
    tickers: str = ''
