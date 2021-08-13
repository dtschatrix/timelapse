from datetime import datetime
import os

from youtube_dl.YoutubeDL import YoutubeDL
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
        self._ydl = YoutubeDL({'format': 'best', 'outtmpl': '%(id)s.%(ext)'})

        threading.Thread.__init__(self, name=name)

    def run(self):
        time.sleep(10)
        if self.isactive:
            with self._ydl:
               try:
                   self._ydl.cache.remove()
                   item_info = self._ydl.extract_info(self.url, download=False)
                   if 'entries' in item_info:
                       video = item_info["entries"]["url"]
                   else:
                       video = item_info["url"]
               except:
                   pass

            time_s = datetime.now().strftime("%H:%M:%S")
            subprocess.call(['ffmpeg',
                             '-i',
                             f'{video}',
                             '-t',
                             f'{self.record_time}',
                             '-c',
                             'copy',
                             '-y',
                             f'{self.path}/{self.name}_{time_s}.mp4'])
            time.sleep(1)
            self._service.add_camera_metadata(
                self.id, f'{self.path}/{self.name}_{time_s}.mp4')
