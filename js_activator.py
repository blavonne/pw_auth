from reader import script_reader


def activate_promo(driver, pins):
    driver.execute_script(script_reader('scripts/library.js'), 'pins', pins)


def send_gifts(driver):
    driver.execute_script(script_reader('scripts/library.js'), 'gifts')
