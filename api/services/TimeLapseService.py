from typing import List
from models.TimeLapse import TimeLapse

from fastapi import (
    Depends,
    HTTPException,
    status
)
from sqlalchemy.orm import Session

import tables as tables
from database import get_session


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

    def create(self, timelapse: TimeLapse) -> TimeLapse:
        timelapse = tables.TimeLapse(**timelapse.dict())
        self.session.add(timelapse)
        self.session.commit()
        return timelapse

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
