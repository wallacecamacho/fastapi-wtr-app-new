import yfinance as yf
from app.db.errors import StocksYFinanceException
from loguru import logger


class Stocks:
    def __init__(self, ticker, start=None, end=None):
        """Classe para buscar os dados do yfinance.

        Utilizada para buscar os dados do ativos pelo yfinance.

        Args:
            ticker (_type_): ticker usado para consultar os indices
            start (date, optional): Data inicial . Defaults to None.
            end (date, optional): Data final. Defaults to None.
        """

        self.ticker = ticker
        self.start = start
        self.end = end

        try:
            self._tickers = yf.Tickers(self.ticker)
            self.df = self.df_ = self._tickers

            quotes = []
            quotes = self.ticker
            quotes = quotes.strip().split(',')
            quotes = ' '.join(quotes).strip()

            hist = {}
            news = {}
            tickersObj = self.df
            for x in tickersObj.tickers:
                if not (self.start or self.end):
                    hist[x] = tickersObj.tickers[x].history(
                        period='max', auto_adjust=True
                    )
                else:
                    hist[x] = tickersObj.tickers[x].history(
                        start=self.start, end=self.end, auto_adjust=True
                    )
                hist[x]['Date'] = hist[x].index.to_pydatetime()
                hist[x] = hist[x].to_dict(orient='records')
                #news[x] = tickersObj.tickers[x].news
            self.tickers = hist
            self.news = news

        except Exception:
            logger.error('Error to try stock yfinance')
            raise StocksYFinanceException('class Stocks error get yfinance')

    def news_tickers(self):
        news = {}
        try:
            tickersObj = self.df
            for x in tickersObj.tickers:
                news[x] = tickersObj.tickers[x].news
        except Exception:
            logger.error('Error to try stock yfinance')
            raise StocksYFinanceException('class Stocks error get yfinance')
        finally:
            return news


class Stock(Stocks):
    def __init__(self, ticker, start=None, end=None):
        self.ticker = ticker
        try:
            self._ticker = yf.Ticker(self.ticker)
            self.df = self.df_ = self._ticker
            if not (self.start or self.end):
                self.df = self.df_ = self._ticker.history(
                    period='max', auto_adjust=True
                )

            else:
                self.df = self.df_ = self._ticker.history(
                    start=self.start, end=self.end, auto_adjust=True
                )

        except Exception:
            logger.error('Error to try stock yfinance')
            raise StocksYFinanceException('class Stocks error get yfinance')
