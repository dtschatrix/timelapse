from typing import List
from models.LiveViews import LiveViews

from fastapi import (
    Depends,
    HTTPException,
    status
)
from sqlalchemy.orm import Session

import liveviews.tables as tables
from liveviews.database import get_session


class LiveViewsService:
    def __init__(self, session: Session = Depends(get_session)) -> List[tables.LiveViews]:
        self.session = session

    def get_list(self) -> List[LiveViews]:
        entities = (
            self.session
            .query(tables.LiveViews)
            .all()
        )
        return entities

    def get_by_id(self, id) -> LiveViews:
        liveViews = (
            self.session
            .query(tables.LiveViews)
            .filter_by(id=id)
            .first()
        )
        if not liveViews:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return liveViews

    def add_view(self, live_view: LiveViews) -> LiveViews:
        liveview = tables.LiveViews(**live_view.dict())
        self.session.add(liveview)
        self.session.commit()
