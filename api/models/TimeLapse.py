from typing import Optional
from pydantic import BaseModel


class BaseTimeLapse(BaseModel):
    camera_id: int
    path: str
    file_size: int
    fps: float
    comment: Optional[str]


class TimeLapseCreate(BaseTimeLapse):
    pass


class TimeLapse(BaseTimeLapse):
    id: int

    class Config:
        orm_mode = True
