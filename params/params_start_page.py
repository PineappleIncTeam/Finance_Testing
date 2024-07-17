"""Start page params"""
import pytest
from pages.start_page import StartPage
from pages.main import Main

sp = StartPage(Main)

header_links = [
    pytest.param(Main.ABOUT_US_LNK, f"{sp.base_url}aboutUs", id="About Us"),
    pytest.param(Main.BLOG_LNK, f"{sp.base_url}blog", id="Blog"),
    pytest.param(Main.ABOUT_APP_LNK, f"{sp.base_url}aboutApp", id="About app"),
    pytest.param(Main.ENTER_BTN, f"{sp.base_url}login", id="Login"),
    pytest.param(Main.REGISTER_BTN, f"{sp.base_url}signUp", id="Registration"),
]

header_lnk = [
    pytest.param(Main.MAIN_LOGO, id="Logo icon"),
    pytest.param(Main.MAIN_LNK, id="Main link")
]

start_img_pc = [
        pytest.param(Main.MAIN_LOGO, id="Logo img"),
        pytest.param(StartPage.START_PICTURE, id='Main img')
]

resolution = [
    pytest.param(1920, 1080, id="1920x1080"),
    pytest.param(1440, 960, id="1440x960"),
    pytest.param(1024, 1366, id="1024x1366"),
    pytest.param(768, 1024, id="768x1024"),
    pytest.param(360, 640, id="360x640")
]


window_width = [
        pytest.param(1025, 960, id="1025"),
        pytest.param(1280, 960, id="1280"),
        pytest.param(1366, 960, id="1366"),
        pytest.param(1440, 960, id="1440"),
        pytest.param(1920, 960, id="1920")
]

window_height = [
        pytest.param(1025, 960, id="960"),
        pytest.param(1025, 500, id="500")
]

window_width_navbar = [
        pytest.param(1024, 1366, id="1024x1366"),
        pytest.param(900, 1024,  id="900x1024"),
        pytest.param(768, 1024, id="768x1024"),
        pytest.param(500, 640, id="500x640"),
        pytest.param(360, 640, id="360x640"),
        pytest.param(359, 640, id="359x640")
]
