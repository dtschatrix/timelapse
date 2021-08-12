import time
from services.MetadataService import MetadataService
from settings import settings

def main():
    meta_service = MetadataService(settings.VIDEO_PATH)
    print("run")
    while 1:
        time.sleep(int(10))
        meta_service.build_timelapse_of_day()
        


if __name__ == "__main__":
    main()
