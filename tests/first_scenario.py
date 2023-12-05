from consts import SBIS_PAGE_URL
from pages.locators import TensorPageLocators, SbisPageLocators
from pages.sbis_page import SbisPage


def test_first_scenario(browser):
   sbis_page = SbisPage(driver=browser, base_url=SBIS_PAGE_URL)
   sbis_page.open_page()
   sbis_page.go_to_contacts_page(locator=SbisPageLocators.CONTACTS_PAGE_LINK)
   sbis_page.go_to_tensor_page(locator=TensorPageLocators.TENSOR_BANNER_IMG)
   sbis_page.should_block_strength_is_in_people(
      locator=TensorPageLocators.STRENGTH_IS_IN_PEOPLE_BLOCK
   )
   sbis_page.should_strength_is_in_people_about_open(
      locator=TensorPageLocators.STRENGTH_IS_IN_PEOPLE_ABOUT
   )
   sbis_page.should_img_identical_sizes(locator=TensorPageLocators.WORKING_BLOCK)
