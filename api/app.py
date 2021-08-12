from db import tasks
from tablehelper import fill_up_base, tables_exist
from fastapi import FastAPI
from database import engine
from tables import Base
from controllers import Camera, LiveViews, TimeLapse


if not tables_exist():
    Base.metadata.create_all(engine)
    fill_up_base()


app = FastAPI()

app.add_event_handler("startup", tasks.create_start_app_handler(app))
app.add_event_handler("shutdown", tasks.create_stop_app_handler(app))

app.include_router(Camera.router)
app.include_router(LiveViews.router)
app.include_router(TimeLapse.router)
