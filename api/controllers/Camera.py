from starlette import status
from services.CameraService import CameraService
from models.Camera import Camera, CameraCreate
from fastapi import APIRouter, Depends
from typing import List

router = APIRouter(
    prefix="/cameras"
)


@router.get("/", response_model=List[Camera])
def get_cameras(service: CameraService = Depends()):
    return service.get_list()


@router.get("/{id}", response_model=Camera)
def get_cameras_by_id(id: int, service: CameraService = Depends()):
    return service.get_by_id(id)


@router.post("/", response_model=Camera)
def add_camera(
    cameras_data: CameraCreate,
    service: CameraService = Depends()
):
    return service.create(cameras_data)


@router.put("/{id}")
def change_status_camera(id: int, service: CameraService = Depends()):
    service.change_status(id)
    return status.HTTP_204_NO_CONTENT
