import time


class Scheduler():
    def __init__(self, time: int) -> None:
        self.time = time

    def run(self, func, **kwargs):
            func(**kwargs)
            time.sleep(self.time)
