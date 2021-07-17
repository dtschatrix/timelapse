import threading
from datetime import datetime
import subprocess
import time


class VideoThread(threading.Thread):
    def __init__(self, stop_event, video, path, name="MyThread") -> None:
        super(VideoThread, self).__init__()
        self._sleepperiod = 1.0
        self.stop_event = stop_event
        self.video = video
        self.name = name
        self.path = path
        self.isactive = True

        threading.Thread.__init__(self, name=name)

    def run(self):
        while not self.stop_event.is_set():
            if self.isactive:
                time_s = datetime.now().strftime("%H:%M:%S")
                subprocess.call(['ffmpeg', '-y', '-i', self.video['url'], '-c:v',
                                 'copy', '-c:a', 'copy', f'{self.path}/pudgebeatbox_{time_s}.mp4'])
                time.sleep(1)

    def join(self, timeout=None):
        self._stopevent.set()
        threading.Thread.join(self, timeout)
