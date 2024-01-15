import pytest
from selene import browser


@pytest.fixture(autouse=True)
def setup():
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield browser

    browser.quit()


# @pytest.fixture
# def browser():
