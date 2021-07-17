from .BaseModel import BaseModels


class Camera(BaseModels):
    camera_name: str
    stream_url: str
    is_active: bool


    
