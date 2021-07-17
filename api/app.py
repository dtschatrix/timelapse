import liveviews
from video.tablehelper import fill_up_base
from fastapi import FastAPI
from sqlalchemy_utils.functions.database import database_exists
from video.database import engine
from video.tables import Base
from .api import router

if not database_exists(engine.url):
    Base.metadata.create_all(engine)
    fill_up_base()


app = FastAPI()
app.include_router(router)


