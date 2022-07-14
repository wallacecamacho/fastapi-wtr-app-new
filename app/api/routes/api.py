from app.api.routes import authentication, profiles, tickers, users
from fastapi import APIRouter

router = APIRouter()
router.include_router(authentication.router, tags=['authentication'], prefix='/users')
router.include_router(users.router, tags=['users'], prefix='/user')
router.include_router(profiles.router, tags=['profiles'], prefix='/profiles')
router.include_router(tickers.router, tags=['tickers'], prefix='/tickers')
