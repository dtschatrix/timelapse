from pydantic.main import BaseModel


class BaseCamera(BaseModel):
    camera_name: str
    stream_url: str
    is_active: bool


class Camera(BaseCamera):
    id: int

    class Config:
        orm_mode = True


class CameraCreate(BaseCamera):
    pass
