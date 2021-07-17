from typing import List
from video.api.models.time_lapse import TimeLapse

from fastapi import (
    Depends,
    HTTPException,
    status
)
from sqlalchemy.orm import Session

from video import tables
from video.database import get_session


class TimeLapseService:
    def __init__(self, session: Session = Depends(get_session)) -> List[tables.Cameras]:
        self.session = session

    def get_list(self) -> List[tables.TimeLapse]:
        entities = (
            self.session
            .query(tables.TimeLapse)
            .all()
        )
        return entities

    def get_by_id(self, id) -> TimeLapse:
        timelpase = (
            self.session
            .query(tables.TimeLapse)
            .filter_by(id=id)
            .first()
        )
        if not timelpase:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return timelpase

    def change_comment(self, id: int, comment: str) -> None:
        timelapse = (
            self.session
            .query(tables.TimeLapse)
            .filter_by(id=id)
            .first()
        )
        if not timelapse:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        try:
            timelapse.comment = comment
            self.session.add(timelapse)
            self.session.commit()
        except:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
