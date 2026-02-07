import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.mark.qatouch("n8bKxG")
def test_verify_login_title():

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        driver.get("https://www.google.com")

        driver.maximize_window()

        title = driver.title
        print("Page Title:", title)

        assert "Google" in title

    finally:
        driver.quit()
