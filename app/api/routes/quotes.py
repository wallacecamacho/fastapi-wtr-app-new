from fastapi import APIRouter, Depends

from app.api.dependencies.database import get_repository
from app.db.repositories.ticker import TickerRepository
from app.models.schemas.quotes import Quotes

router = APIRouter()


@router.get("", response_model=Quotes, name="tickers:get-all")
async def get_all_tickers(
    tickers_repo: TickerRepository = Depends(get_repository(TickerRepository)),
) -> Quotes:
    tickers = await tickers_repo.get_all_ticker()
    return Quotes(tickers=tickers)
