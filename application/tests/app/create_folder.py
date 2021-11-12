import dataclasses
import os
from typing import List, Tuple
from app.folder import Folder


@dataclasses.dataclass
class CreateFolder:
    name: str
    file_format: Tuple[str]
    path: str

    def __call__(self) -> Folder:
        folder = Folder(name=self.name, file_format=self.file_format, path=self.path)
        return folder

    @classmethod
    def create_folder(cls, list_folder: List[Folder]) -> bool:
        for folder in list_folder:
            os.makedirs(folder )
        return True
