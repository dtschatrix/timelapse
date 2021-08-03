import time


class Scheduler():
    def __init__(self, time: int) -> None:
        self.time = time

    def run(self, camera_func, **kwargs):
        camera_func(**kwargs)
        time.sleep(self.time)
