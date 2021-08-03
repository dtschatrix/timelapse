from pydantic.main import BaseModel


class BaseLiveViews(BaseModel):
    camera_id: int
    path: str
    file_size: int
    fps: float


class LiveViewsCreate(BaseLiveViews):
    pass


class LiveViews(BaseLiveViews):
    id: int

    class Config:
        orm_mode = True
