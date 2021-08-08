from datetime import datetime
from services.MetadataService import MetadataService
import subprocess
import threading
import time


class Video(threading.Thread):
    def __init__(self, id: int, name: str, stop_event: threading.Event, url: str, path: str, record_time: int) -> None:
        super(Video, self).__init__()
        self.id = id
        self.name = name
        self.stop_event = stop_event
        self.url = url
        self.path = path
        self.isactive = True
        self.record_time = record_time
        self._service = MetadataService()

        threading.Thread.__init__(self, name=name)

    def run(self):
        if self.isactive:
            time_s = datetime.now().strftime("%H:%M:%S")
            subprocess.call(['ffmpeg',
                             '-i',
                             f'{self.url}',
                             '-t',
                             f'{self.record_time}',
                             '-c',
                             'copy',
                             '-y',
                             f'{self.path}/{self.name}_{time_s}.mp4'])
            time.sleep(1)
            self._service.add_camera_metadata(self.id, self.path)
