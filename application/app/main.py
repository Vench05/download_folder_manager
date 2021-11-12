import os
from pathlib import Path
from typing import List

from create_folder import CreateFolder


users_download_folder = os.path.join(Path.home(), 'Downloads')


def get_default_create_folder() -> List[dict]:
    return [
        {
            'name': 'exe_files',
            'file_format': ('exe'),
        },
        {
            'name': 'Archieve_files',
            'file_format': ('zip', 'rar', '7z'),
        },
        {
            'name': 'Pictures',
            'file_format': ("jpg", "jpeg", "png", "gif"),
        },
        {
            'name': 'Documents',
            'file_format': ("docx", "doc", "pdf", "pptx"),
        },
    ]

def main():
    if os.path.isdir(users_download_folder):
        default_create_folder = get_default_create_folder()
        
        for folder in default_create_folder:
            folder = CreateFolder(**folder)()
            CreateFolder.create_folder(folder=folder, user_download_path=users_download_folder)
            folder.move_to_folder(user_download_path=users_download_folder)

    else:
        raise Exception


if __name__ == '__main__':
    main()
    os.startfile(users_download_folder)
    