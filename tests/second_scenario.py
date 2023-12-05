from consts import SBIS_PAGE_URL, MY_REGION
from pages.locators import SbisPageLocators
from pages.sbis_page import SbisPage


def test_second_scenario(browser):
    sbis_page = SbisPage(driver=browser, base_url=SBIS_PAGE_URL)
    sbis_page.open_page()
    sbis_page.go_to_contacts_page(locator=SbisPageLocators.CONTACTS_PAGE_LINK)
    sbis_page.should_my_region_defined(
        locator=SbisPageLocators.REGION_DEFINED, my_region=MY_REGION
    )

    regions_partners = {MY_REGION: []}
    regions_partners[MY_REGION] = sbis_page.should_my_region_partners_list_exists(
        locator=SbisPageLocators.PARTNERS_LIST
    )
    sbis_page.choose_kamchatka_region(locator=SbisPageLocators.KAMCHATKA_REGION_ITEM)
    sbis_page.should_region_changes_applied(
        my_region_partners=regions_partners[MY_REGION]
    )