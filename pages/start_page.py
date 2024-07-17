import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.main import Main


class StartPage(Main):

    def __init__(self, driver):
        super().__init__(driver)

    START_BODY_CONTAINER = "//div[@class='service_mainPageContainer__1EH2p']"
    START_PICTURE = "(//div/img)[1]"
    START_TEXT_CONTAINER = "(//h1[contains(text(), 'Наслаждайся расходами')])[1]"

    @allure.step("Check image visibility")
    def check_image_visibility(self, element, driver):
        """Check image displayed and visible"""
        try:
            WebDriverWait(driver, 10).until(EC.visibility_of(element))
            # Check if the element is displayed
            if not element.is_displayed():
                print("Image is not visible.")
                return False

            # Check the image loading status
            scrptW = "return arguments[0].naturalWidth;"
            scrptH = "return arguments[0].naturalHeight;"

            natural_width = driver.execute_script(scrptW, element)
            natural_height = driver.execute_script(scrptH, element)
            if natural_width == 0 or natural_height == 0:
                print("Image is not loaded correctly.")
                return False

            # Check if the image is fully transparent
            opacity = driver.execute_script("return window.getComputedStyle(arguments[0]).getPropertyValue('opacity');",
                                            element)
            if float(opacity) == 0:
                print("Image is fully transparent.")
                return False

            # Check if the image has visibility: hidden or display: none
            visibility = driver.execute_script(
                "return window.getComputedStyle(arguments[0]).getPropertyValue('visibility');", element)
            display = driver.execute_script("return window.getComputedStyle(arguments[0]).getPropertyValue('display');",
                                            element)
            if visibility == 'hidden' or display == 'none':
                print("Image is hidden or not displayed.")
                return False

            return True
        except Exception as e:
            print(f"Error checking image visibility: {e}")
            return False
