import pytest
from selenium import webdriver
import time


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language for site")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    if language in ["ar", "ca", "cs", "da", "de", "en-gb", "el", "es", "fi", "fr", "it", "ko", "nl",
                    "pl", "pt", "pt-br", "ro", "ru", "sk", "uk", "zh-cn"]:
        print("\nstart chrome browser for test..")
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError("--language wrong")
    yield browser
    time.sleep(5)
    print("\nquit browser..")
    browser.quit()
