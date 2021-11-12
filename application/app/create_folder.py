import dataclasses
import os
from typing import Tuple

from folder import Folder


@dataclasses.dataclass
class CreateFolder:
    name: str
    file_format: Tuple[str]

    def __call__(self) -> Folder:
        folder = Folder(name=self.name, file_format=self.file_format)
        return folder

    @classmethod
    def create_folder(cls, folder: Folder, user_download_path: str) -> bool:
        path = os.path.join(user_download_path, folder.name)
        if os.path.isdir(path):
            return False
        os.makedirs(path)
        return True
