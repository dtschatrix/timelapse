from services.CameraService import CameraService
from runner import run_cameras
from scheduler import Scheduler
from database import get_session
import os


def main():
    print(os.getenv("video_path"))
    scheduler = Scheduler(60)
    camera_service = CameraService(get_session().__next__())
    while 1:
        cameras = camera_service.get_active_cameras()
        scheduler.run(run_cameras, active_cameras=cameras)


if __name__ == "__main__":
    main()
