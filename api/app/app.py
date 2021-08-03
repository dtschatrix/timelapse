from tablehelper import fill_up_base, tables_exist
from fastapi import FastAPI
from database import engine
from tables import Base
from controllers import cameras, live_views, timelapse

if not tables_exist():
    Base.metadata.create_all(engine)
    fill_up_base()


app = FastAPI()
app.include_router(cameras.router)
app.include_router(live_views.router)
app.include_router(timelapse.router)


