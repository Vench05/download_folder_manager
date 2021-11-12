import os
from app import create_folder
from app import app

import tempfile

def test_main(monkeypatch):
    temp_dir = os.path.join(tempfile.gettempdir(), 'Downloads')
    if not os.path.isdir(temp_dir):
        os.makedirs(temp_dir)
    monkeypatch.setattr(app, 'users_download_folder', temp_dir)
    app.main()
    assert True
