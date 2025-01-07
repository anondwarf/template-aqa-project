from dotenv import load_dotenv

load_dotenv()

pytest_plugins = [
    "src.ui.fixtures.page",
    "src.ui.fixtures.user_auth",
]
