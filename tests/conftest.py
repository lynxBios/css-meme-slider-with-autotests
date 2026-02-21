import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope='function')
    # Fixture for creating a browser instance.
    # scope="function" means that the browser will be opened fresh for each test.

def browser():
    # 1. Setup: create Service object

    print("\nStarting browser for test...")
    service = Service(ChromeDriverManager().install())
    options = Options()

    options.add_argument('--headless')  # Run without graphical window
    options.add_argument('--disable-gpu')  # Disable GPU
    options.add_argument('--no-sandbox')  # Required for running in Linux containers
    options.add_argument('--disable-dev-shm-usage')  # Solves memory shortage issues in containers

    # 2. Initialization: start browser
    # Manager will automatically find, download and set the driver path
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10)

    # 3. Hand over control to test
    # Here the test "takes" the browser and performs its actions
    yield driver

    # 4. Teardown: close browser
    driver.quit()
    print(' Browser closed')
