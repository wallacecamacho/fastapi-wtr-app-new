class EntityDoesNotExist(Exception):
    """Raised when entity was not found in database."""


class StocksYFinanceException(Exception):
    """Raise when Stock was not found in API.

    Args:
        Exception (_type_): Failed to get stocks in a lib yfinance.
    """
