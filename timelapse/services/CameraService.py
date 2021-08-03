from typing import List
from timelapse.models.Camera import Camera

from fastapi import (
    Depends,
    HTTPException,
    status
)
from sqlalchemy.orm import Session

import timelapse.tables as tables
from timelapse.database import get_session


class CameraService:
    def __init__(self, session: Session = Depends(get_session)) -> List[tables.Cameras]:
        self.session = session

    def get_list(self) -> List[Camera]:
        entities = (
            self.session
            .query(tables.Cameras)
            .all()
        )
        return entities

    def get_by_id(self, id) -> Camera:
        camera = (
            self.session
            .query(tables.Cameras)
            .filter_by(id=id)
            .first()
        )
        if not camera:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return camera

    def get_active_cameras(self) -> List[Camera]:
        cameras = (
            self.session
            .query(tables.Cameras)
            .filter_by(is_active=True)
            .all()
        )
        if not cameras:
            raise
        return cameras

    def create(self, cameras_data: Camera) -> tables.Cameras:
        cameras = tables.Cameras(**cameras_data.dict())
        self.session.add(cameras)
        self.session.commit()
        return cameras

    def change_status(self, id: int) -> None:
        camera = (
            self.session
            .query(tables.Cameras)
            .filter_by(id=id)
            .first()
        )
        if not camera:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        try:
            camera.is_active = not camera.is_active
            self.session.add(camera)
            self.session.commit()
        except:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get_id_by_name(self, camera_name: str) -> int:
        camera = (
            self.session
            .query(tables.Cameras)
            .filter_by(camera_name = camera_name)
            .first()
        )
        if not camera:
            raise Exception
        
        return camera.id
