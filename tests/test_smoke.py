from selenium.webdriver.common.by import By

def test_page_title(browser):
    
    # Check that the page opens and has a correct title.
    # We use GitHub Pages or local file.    
    # Replace with your published site URL or path to local file
    url = 'http://localhost:8000'

    browser.get(url)

    # Check that the tab title contains the expected word
    expected_title = 'CSS Meme Slider'
    assert expected_title == browser.title, f'Expected "{expected_title}", but got "{browser.title}"'
