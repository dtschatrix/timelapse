from typing import List
from video.tables import TimeLapse
from fastapi.param_functions import Depends
from services.TimeLapseService import TimeLapseService
from fastapi import APIRouter


router = APIRouter(
    prefix="/timelapse"
)


@router.get("/", response_model=List[TimeLapse])
def get_timelapses(service: TimeLapseService = Depends()) -> List[TimeLapse]:
    return service.get_list()


@router.get("/{id}")
def get_timelpase_by_id(timelapse_id: int, service: TimeLapseService = Depends()) -> TimeLapse:
    return service.get_by_id(timelapse_id)


@router.put("/{id}")
def change_timelapse_comment_by_id(timelapse_id: int, comment: str, service: TimeLapseService = Depends()):
    return service.change_comment(timelapse_id, comment)
