import time
from services.MetadataService import MetadataService
from settings import settings
import os


def main():
    meta_service = MetadataService(settings.VIDEO_PATH)
    while 1:
        print("run")
        time.sleep(float(os.environ["timelapse_delay"]))
        meta_service.build_timelapse_of_day()


if __name__ == "__main__":
    main()
