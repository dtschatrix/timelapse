from services.CameraService import CameraService

from datetime import datetime
import os
import subprocess
from ffprobe import FFProbe

from database import get_session
from services.TimeLapseService import TimeLapseService
from models.TimeLapse import TimeLapseCreate
from services.DirectoryService import DirectoryService


class MetadataService:
    def __init__(self, path: str = "") -> None:
        self.__dir_service = DirectoryService()
        self.path = path
        pass


    def __add_timelapse_metadata(self, path: str, directory: str):
        file = FFProbe(path)
        
        if file:
            try:
                camera_service = CameraService(get_session().__next__())
                camera_id = camera_service.get_id_by_name(self.__get_camera_name(directory))

                time_lapse_service = TimeLapseService(get_session().__next__())
                
                
                framerate = self.__get_framerate(file)
                metadata = TimeLapseCreate(camera_id=camera_id, path=file.path_to_video,
                                           file_size=os.path.getsize(file.path_to_video), fps=float(framerate))

                time_lapse_service.create(metadata)

            except:
                raise AttributeError()

    def __get_framerate(self, file: FFProbe):
        video_stream = next(
            (stream for stream in file.streams if stream.codec_type == 'video'), None)
        if video_stream is None:
            print('No video stream found!')
            return
        return video_stream.framerate

    def build_timelapse_of_day(self):
        dirs = self.__dir_service.get_last_directories(self.path)
        for directory in dirs:
            videos = []
            for video in self.__dir_service.get_files_from_directory(directory):
                self.__build_timelapse(video, directory)
                videos.append(f'file timelapse{video}')

            if videos:

                videos_path = "\n".join(sorted(videos))
                f = open(f'{directory}/{os.environ["timelapse_links"]}', 'w')
                f.write(videos_path)
                f.close()
                
                date = datetime.now().strftime("%H:%M:%S")

                subprocess.call(['ffmpeg',
                                '-f',
                                 "concat",
                                 "-safe",
                                 "0",
                                 '-i',
                                 os.environ["timelapse_links"],
                                 "-c",
                                 "copy",
                                 f'timelapse_{date}.mp4'],
                                cwd=os.getcwd() + f'/{directory}')
                
                self.__add_timelapse_metadata(os.getcwd()+ f'/{directory}' + f'/timelapse_{date}.mp4', directory)


    def __build_timelapse(self, video, directory):
        subprocess.call(['ffmpeg',
                         '-i',
                         f'{video}',
                         '-filter:v',
                         'setpts=0.1*PTS',
                         '-an',
                         f"timelapse{video}"],
                        cwd=os.getcwd() + f'/{directory}')


    def __get_camera_name(self,directory: str) -> str:
        return directory.split("/")[-1]