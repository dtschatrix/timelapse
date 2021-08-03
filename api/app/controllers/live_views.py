from typing import List
from models.live_views import LiveViews
from services.LiveViewsService import LiveViewsService
from fastapi.param_functions import Depends
from fastapi import APIRouter

router = APIRouter(
    prefix="/liveviews"
)


@router.get("/", response_model=List[LiveViews])
def get_live_views(service: LiveViewsService = Depends()) -> List[LiveViews]:
    return service.get_list()


@router.get("/{id}", response_model=LiveViews)
def get_live_views_by_id(live_views_id: int, service: LiveViewsService = Depends()) -> LiveViews:
    return service.get_by_id(live_views_id)
