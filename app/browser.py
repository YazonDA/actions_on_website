from random import randint
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from typing import Dict


class Browser:
    def __init__(self, browser_type: str = 'chrome'):
        self.option = Options()
        self.option.add_argument(
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
        )
        self.option.add_argument('--disable-blink-features=AutomationControlled')
        self.option.add_experimental_option('detach', True)
        self.__choose_webdriver(browser_type)

    def __choose_webdriver(self, browser_type: str):
        if browser_type == 'firefox':
            self.browser = webdriver.Firefox()
        elif browser_type == 'chrome':
            self.browser = webdriver.Chrome()
        else:
            print('ERROR!\nSomething is wrong!\nUnknow browser type!')
            exit(1)

    def check_ready_to_update(self) -> bool:
        return True

    def take_screenshoot(self, img_path: str = '~/Pictures/image_for_save.png'):
        self.browser.save_screenshot(img_path)

    def open_page(self, url_: str):
        self.browser.get(url_)

    def get_element_from_page(self, labels_: str):
        return self.browser.find_element_by_xpath(labels_)

    def action_on_page(self, this_step: dict):
        elem = ''
        if this_step['url']:
            self.open_page(this_step['url'])
            sleep(randint(1, 3))
        if this_step['xpath']:
            elem = self.get_element_from_page(this_step['xpath'])
            sleep(randint(1, 3))
        if elem:
            if this_step['data'] == 'Keys.RETURN':
                elem.send_keys(Keys.RETURN)
            elif this_step['data']:
                elem.send_keys(this_step['data'])
        sleep(randint(1, 3))


if __name__ == '__main__':
    print('This is not executable module!')
