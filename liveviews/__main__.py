from services import CameraService
from liveviews.runner import run_cameras
from liveviews.scheduler import Scheduler
from video.database import get_session


def main():
    scheduler = Scheduler(60)
    service = CameraService.CameraService(get_session().__next__())
    
    while 1:
        cameras = service.get_active_cameras()
        scheduler.run(run_cameras,active_cameras=cameras)


if __name__ == "__main__":
    main()
