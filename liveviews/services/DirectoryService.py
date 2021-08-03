from glob import glob
import os
from ffprobe.ffprobe import FFProbe


class DirectoryService:
    def __init__(self) -> None:
        pass

    def get_files_from_directory(self, path):
        list_of_files = [file for file in os.listdir(path) if file.endswith(
            ".mp4") and not file.startswith("timelapse")]
        
        if list_of_files:
            return list_of_files

        return None

    def get_last_file(self, path):
        last_file = sorted(os.listdir(path))[-1]

        return FFProbe(f'{path}/{last_file}')

    def get_last_directories(self, path):
        list_of_dirs = filter(os.path.isdir, glob(path + '/*'))

        return sorted(list_of_dirs)
