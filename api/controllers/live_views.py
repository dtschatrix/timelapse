from typing import List
from video.tables import LiveViews
from services.LiveViewsService import LiveViewsService
from fastapi.param_functions import Depends
from fastapi import APIRouter

router = APIRouter(
    prefix="/liveviews"
)


@router.get("/")
def get_live_views(service: LiveViewsService = Depends()) -> List[LiveViews]:
    return service.get_list()


@router.get("/{id}")
def get_live_views_by_id(live_views_id: int, service: LiveViewsService = Depends()) -> LiveViews:
    return service.get_by_id(live_views_id)
