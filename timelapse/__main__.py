import os
import time
from timelapse.services.MetadataService import MetadataService

def main():
    meta_service = MetadataService(os.environ["video_path"])
    print("run")
    while 1:
      #  time.sleep(os.environ["timelapse_delay"])
        meta_service.build_timelapse_of_day()
        


if __name__ == "__main__":
    main()