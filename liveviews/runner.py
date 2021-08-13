from models.Camera import Camera
import os
import threading
from typing import List
from models.Video import Video
from settings import settings


path = settings.VIDEO_PATH
video_duration = os.environ["cam_duration"]


def looper_control(state, stop_event, t):
    if state:
        t.start()
    elif not state:
        stop_event.set()


def run_cameras(active_cameras: List[Camera]):
    threads = []

    for camera in active_cameras:
        camera_path = f'{path}{camera.camera_name}'

        if not os.path.exists(camera_path):
            os.makedirs(camera_path)

        video = Video(
            id=camera.id,
            name=camera.camera_name,
            stop_event=threading.Event(),
            url=camera.stream_url,
            path=camera_path,
            record_time=video_duration)

        threads.append(video)

    for index, camera in enumerate(active_cameras):
        looper_control(camera.is_active, threads[index].stop_event, threads[index])
