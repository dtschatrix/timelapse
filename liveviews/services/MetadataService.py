import os

from database import get_session
from services.LiveViewsService import LiveViewsService

from models.LiveViews import LiveViewsCreate
from services.DirectoryService import DirectoryService


class MetadataService:
    def __init__(self, path: str = "") -> None:
        self.__dir_service = DirectoryService()
        self.path = path
        pass

    def add_camera_metadata(self, id: int, path: str) -> None:
        file = self.__dir_service.get_file_by_name(path)

        if file:
            video_stream = next(
                (stream for stream in file.streams if stream.codec_type == 'video'), None)
            if video_stream is None:
                print('No video stream found!')
                return

            metadata = LiveViewsCreate(camera_id=id, path=file.path_to_video, fps=float(
                video_stream.framerate), file_size=os.path.getsize(file.path_to_video))

            service = LiveViewsService(get_session().__next__())
            service.add_view(metadata)
