from pydantic.main import BaseModel


class BaseModels(BaseModel):
    id: int

    class Config:
        orm_mode = True
