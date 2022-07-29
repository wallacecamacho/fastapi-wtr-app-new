from typing import Optional

from app.db.repositories.ticker import TickerRepository
from app.models.schemas.tickers import TickerInList
from fastapi import APIRouter, Depends

router = APIRouter()


@router.get('/{tickers_id}', response_model=TickerInList, name='tickers:get-all')
async def get_all_tickers(
    tickers_id: str,
    start: Optional[str] = None,
    end: Optional[str] = None,
    tickers_repo: TickerRepository = Depends(TickerRepository),
) -> TickerInList:
    return_ticker = await tickers_repo.get_tickers(tickers_id, start, end)
    return TickerInList(tickers=return_ticker['tickers'])
    #return TickerInList(tickers=return_ticker['tickers'], news=return_ticker['news'])
