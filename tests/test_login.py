from selenium import webdriver
from pages.login_page import LoginPage
from test_data import test_data
import pytest
import time


@pytest.mark.parametrize(
    "username,password",
    test_data
)
def test_login(username, password):

    # print(f"\nTesting: {username} | {password}")

    driver = webdriver.Chrome()

    driver.get(
        "https://practicetestautomation.com/practice-test-login/"
    )

    login = LoginPage(driver)

    login.enter_username(username)
    login.enter_password(password)
    login.click_login()

    time.sleep(2)

    try:

        if "Logged In Successfully" in driver.page_source:

            print("PASS ✅")

        else:

            print("FAIL ❌")

            driver.save_screenshot(
                f"screenshots/{username}.png"
            )

    except Exception as e:

        print("Error:", e)

        driver.save_screenshot(
            f"screenshots/error_{username}.png"
        )

    finally:

        driver.quit()