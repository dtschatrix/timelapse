from typing import Optional
from video.models.BaseModel import BaseModels

class TimeLapse(BaseModels):
    camera_id: int
    path: str
    file_size: int
    fps: float
    comment: Optional[str]


