from fastapi import APIRouter

from .clients import router as users_router

router = APIRouter()
router.include_router(users_router)
