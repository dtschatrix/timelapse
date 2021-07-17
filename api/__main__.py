import uvicorn

from video.settings import settings

uvicorn.run(
    "video.app:app",
    host=settings.server_host,
    port=settings.server_port,
    reload=True
)
