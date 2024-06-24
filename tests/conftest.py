import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="class")
def setup(request):
    option = Options()
    option.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("http://staging.shopping.beeyor.com/shop/")
    request.cls.driver = driver
    yield
    driver.quit()
