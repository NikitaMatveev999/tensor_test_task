from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

    def open_page(self, url=None):
        if not url:
            return self.driver.get(self.base_url)
        return self.driver.get(url)

    def find_element(self, locator, element=None, time=10):
        return WebDriverWait(element if element else self.driver, time).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}"
        )

    def find_elements(self, locator, element=None, time=10):
        return WebDriverWait(element if element else self.driver, time).until(
            EC.presence_of_all_elements_located(locator),
            message=f"Can't find elements by locator {locator}"
        )

    def go_to_section_by_clicking(self, locator, time=10):
        section = self.find_element(locator=locator, time=time)
        section.click()
