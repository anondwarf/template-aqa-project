import os


class Constants(object):
    """Константы"""

    try:
        login = os.getenv("AUTH_LOGIN")
        password = os.getenv("AUTH_PASSWORD")
    except KeyError:
        raise EnvironmentError(
            "AUTH_LOGIN и/или AUTH_PASSWORD должны быть указаны"
        )
