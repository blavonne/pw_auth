import logging

from selenium import webdriver
from js_activator import activate_promo, send_gifts
from mail_auth import mail_auth
from reader import acc_reader, pin_reader


def get_domain(login):
    dog = login.index('@')
    domain = login[dog + 1:]

    return domain


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, filename="py_log.log", filemode="w",
                        format="%(asctime)s %(levelname)s - %(message)s")
    acc = acc_reader()
    pins = pin_reader()

    for i in range(len(acc)):
        driver = webdriver.Chrome()
        login = acc[i].login
        password = acc[i].password
        domain = get_domain(login)  # может вернуть yandex.ru, mail.ru, gmail.com
        logged = False

        if domain in ['mail.ru', 'bk.ru', 'list.ru', 'inbox.ru']:
            logging.info(f"{acc[i].login} - выполняется вход")
            logged = mail_auth(driver, login, password)

        if logged:
            if len(pins) > 0:
                activate_promo(driver, pins)
                logging.info(f"{acc[i].login} - активированы промокоды {pins}")

            send_gifts(driver)

        driver.quit()

