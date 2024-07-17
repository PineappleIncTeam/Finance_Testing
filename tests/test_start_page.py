"""
[TEST CASES:]
    Verify access to site.
    Verify presence of cookies popup window.
    Verify closing of cookies window.
    Verify redirection to Registration page
    clicking Cookie registration button.
    Verify redirection to Wiki Cookie article.
    Verify Header's links redirection".
    Verify redirection to Main page (LOGO, Main link).
    Verify visibility of the images (Logo, Main).
    Verify horizontal page layout (Header's links).
    Verify vertical page layout (Header, body).
    Verify displaying Navbar.
    Verify displaying Navbar menu.
    Verify closing Navbar menu.
    Verify redirection using Navbar menu links.
"""
import time
import allure
import pytest
from params.params_start_page import header_links, \
    header_lnk, start_img_pc, window_width, window_height, \
    window_width_navbar, resolution


class TestStartPage:
    """Start page tests."""

    @pytest.mark.parametrize("width, height", resolution)
    def test_site_access(self, start_p, width, height):
        """Verify access to site."""
        with allure.step("Verify Start page is open in the browser"):
            assert start_p.driver.current_url == start_p.base_url

    @pytest.mark.parametrize("width, height", resolution)
    def test_cookie_wnd_presents(self, start_p, width, height):
        """Verify presence of cookies popup window."""
        with allure.step("Verify presence of cookies popup window"):
            assert start_p.get_element(start_p.COOKIE_CONTAINER).is_displayed()

    @pytest.mark.parametrize("width, height", resolution)
    def test_cookies_closing(self, start_p, width, height):
        """Verify closing of cookies window."""
        with allure.step("Click 'x' btn on Cookies window"):
            start_p.get_element(start_p.COOKIE_X_BTN).click()
            time.sleep(2)

        with allure.step("Verify Cookies window is closed"):
            assert not start_p.get_element(start_p.COOKIE_CONTAINER).is_displayed()

    @pytest.mark.parametrize("width, height", resolution)
    @pytest.mark.parametrize("lnk, exp_url", [header_links[-1]])
    def test_cookies_register_btn(self, start_p, width, height, lnk, exp_url):
        """Verify redirection to Registration page
        clicking Cookie registration button."""
        with allure.step("Click 'Registration button"
                         "in Cookie window'"):
            start_p.get_element(start_p.COOKIE_REG_BTN).click()
            time.sleep(2)

        with allure.step("Verify redirection to Registration page"):
            start_p.is_opened(exp_url)
            assert start_p.driver.current_url == exp_url

    @pytest.mark.parametrize("width, height", resolution)
    def test_redirection_cookie_article(self, start_p, width, height):
        """Verify redirection to Wiki Cookie article."""
        with allure.step("Click 'cookie' link in Cookie popup window"):
            start_p.get_element(start_p.COOKIE_LNK).click()

        with allure.step("Switch to the new opened tab"):
            time.sleep(1)
            start_p.driver.switch_to.window(start_p.driver.window_handles[1])

        with allure.step("Verify redirection to Wiki Cookie article"):
            assert start_p.driver.current_url == start_p.COOKIE_WIKI_URL

    @pytest.mark.parametrize("width, height", resolution[:2])
    @pytest.mark.parametrize("lnk, exp_url", header_links)
    def test_headers_links(self, start_p, width, height, lnk, exp_url):
        """Verify Header's links redirection."""
        with allure.step("Click Header link"):
            start_p.get_element(lnk).click()

        with allure.step(f"Verify redirection to {exp_url}"):
            start_p.is_opened(exp_url)
            assert start_p.driver.current_url == exp_url

    @pytest.mark.parametrize("width, height", resolution[:2])
    @pytest.mark.parametrize('lnk', header_lnk)
    def test_logo_main_redirection(self, start_p, lnk):
        """Verify redirection to Main page (LOGO, Main link)."""
        link = start_p.get_random_link()

        with allure.step("Click random Header link"):
            start_p.get_element(link).click()
            time.sleep(2)

        with allure.step("Click Logo icon/Main lnk"):
            start_p.get_element(lnk).click()

        with allure.step("Verify redirection to Start page url"):
            assert start_p.driver.current_url == start_p.base_url

    @pytest.mark.parametrize("width, height", resolution)
    @pytest.mark.parametrize("img", start_img_pc)
    @pytest.mark.parametrize("browser", [False, True],
                             ids=["normal_mode", "incognito_mode"],
                             indirect=True)
    def test_img_visibility(self, start_p, img, width, height):
        """Verify visibility of the images (Logo, Main)."""
        logo_img = start_p.get_element(img)

        with allure.step("Verify visibility of the image"):
            assert start_p.check_image_visibility(logo_img, start_p.driver)

    @pytest.mark.parametrize('width, height', window_width)
    def test_layout_horizontal(self, start_p, width, height):
        """Verify horizontal page layout (Header's links)."""
        with allure.step("Verify not crossing Header's links"):
            time.sleep(1)
            start_p.get_header_objects()
            i = 0
            while i < len(start_p.objects) - 1:
                right, left = start_p.get_ojb_rect(i, 'x', 'width')
                assert right < left
                i = i + 1

    # @pytest.mark.parametrize("width, height", window_height)
    # def test_layout_vertical(self, start_p, width, height):
    #     """Verify vertical page layout (Header, body)."""
    #     with allure.step("Verify elements not crossing each other"):
    #         time.sleep(1)
    #         start_p.objects = [start_p.HEADER_CONTAINER,
    #                            start_p.START_TEXT_CONTAINER]
    #         top, bottom = start_p.get_ojb_rect(100, 'y', 'height')
    #         assert top < bottom

    @pytest.mark.parametrize('width, height', window_width_navbar)
    def test_navbar_displayed(self, start_p, width, height):
        """Verify displaying Navbar."""
        with allure.step("Verify displaying Navbar"):
            navbar = start_p.get_element(start_p.NAVBAR_BURGER)
            assert navbar.is_displayed()

    @pytest.mark.parametrize('width, height', window_width_navbar)
    def test_navbar_menu(self, start_p, width, height):
        """Verify displaying Navbar menu."""
        with allure.step("Click Navbar meny icon"):
            start_p.get_element(start_p.NAVBAR_BURGER).click()

        with allure.step("Verify displaying Navbar menu"):
            navbar_menu_txt = start_p.get_element(start_p.NAVBAR_MENU_TXT)
            assert navbar_menu_txt.is_displayed()

    @pytest.mark.parametrize('width, height', window_width_navbar)
    def test_navbar_menu_closing(self, start_p, width, height):
        """Verify closing Navbar menu."""
        with allure.step("Click Navbar meny icon"):
            start_p.get_element(start_p.NAVBAR_BURGER).click()

        with allure.step("Click Navbar X button"):
            start_p.wait_and_click(start_p.NAVBAR_X_BTN)

        with allure.step("Verify closing Navbar menu"):
            assert start_p.wait_not_present(start_p.NAVBAR_X_BTN)

    @pytest.mark.parametrize("lnk, exp_url", header_links)
    @pytest.mark.parametrize('width, height', window_width_navbar)
    def test_navbar_menu_links(self, start_p, width, height, lnk, exp_url):
        """Verify redirection using Navbar menu links."""
        with allure.step("Click Navbar meny icon"):
            start_p.get_element(start_p.NAVBAR_BURGER).click()

        with allure.step("Click Navbar meny link"):
            start_p.get_element(lnk).click()

        with allure.step(f"Verify redirection to {exp_url}"):
            start_p.is_opened(exp_url)
            assert start_p.driver.current_url == exp_url
