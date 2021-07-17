from fastapi import APIRouter
from .cameras import router as camera_router

router = APIRouter()
router.include_router(router=camera_router)
