import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait_for_elem(driver, locator, query):
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((locator, query))
    )

    return element


def mail_auth(driver, login, password):
    driver.get(
        "https://account.vkplay.ru/oauth2/?redirect_uri=https://pw.mail.ru/oauth2.php&continue&client_id=pw.mail.ru"
        "&response_type=code&show_auth_btn=mailru")

    mail_auth_btn = wait_for_elem(driver, By.CLASS_NAME, "ph-social-btn__text")
    mail_auth_btn.click()

    driver.switch_to.window(driver.window_handles[1])
    login_input = wait_for_elem(driver, By.NAME, 'username')
    login_input.send_keys(login)

    btn = wait_for_elem(driver, By.XPATH, '//button[@data-test-id="next-button"]')
    btn.click()

    password_input = wait_for_elem(driver, By.NAME, 'password')
    password_input.send_keys(password)

    btn = wait_for_elem(driver, By.XPATH, '//button[@data-test-id="submit-button"]')
    btn.click()

    time.sleep(2)
    driver.switch_to.window(driver.window_handles[0])

    btn = wait_for_elem(driver, By.CLASS_NAME, 'ph-form__btn')
    btn.click()

    driver.get('https://pw.mail.ru')

    return True


