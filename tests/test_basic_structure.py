from selenium.webdriver.common.by import By


BASE_URL = "http://localhost:8000"


def test_basic_page_structure(browser):
    browser.get(BASE_URL)

    # 1. Verify that the page has loaded
    assert browser.title != "", "Page title is empty"

    images = browser.find_elements(By.TAG_NAME, "img")
    assert len(images) > 0, "No images found on the page"
        