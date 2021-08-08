from tablehelper import fill_up_base, tables_exist
from fastapi import FastAPI
from database import engine
from tables import Base
from controllers import Camera, LiveViews, TimeLapse

if not tables_exist():
    Base.metadata.create_all(engine)
    fill_up_base()


app = FastAPI()
app.include_router(Camera.router)
app.include_router(LiveViews.router)
app.include_router(TimeLapse.router)


