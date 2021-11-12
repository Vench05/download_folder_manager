import datetime
import uuid
import os
import shutil

from dataclasses import dataclass
from typing import Tuple


@dataclass
class Folder:
    name: str
    file_format: Tuple[str]
    id: str = uuid.uuid4()
    date_modified: datetime.datetime = datetime.datetime.now()

    def __str__(self):
        return f'{self.name}: {self.file_format}'

    def move_to_folder(self, user_download_path: str):
        path = os.path.join(user_download_path, self.name)
        if os.path.isdir(path):
            for file in os.listdir(user_download_path):
                if file.endswith(self.file_format):
                    shutil.move(os.path.join(user_download_path, file), path)
