import os
from pathlib import Path


class Constants(object):
    root_path = Path(__file__).parents[3]
    tmp_path = root_path / "tmp"
    try:
        base_url_ui = os.getenv("BASE_URL_UI")
    except KeyError:
        raise EnvironmentError("BASE_URL_UI не установлен")
