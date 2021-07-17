from .BaseModel import BaseModels

class LiveViews(BaseModels):
    camera_id: int
    path: str
    file_size: int
    fps: float
    