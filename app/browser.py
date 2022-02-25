from random import randint
from time import sleep
from datetime import datetime
from pathlib import Path

import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


class Browser:
    def __init__(self, _config: dict):
        self.__set_browser_type()
        self.__set_header(_config)
        self.__hide_browser_face()
        self.__set_browser()

    def __set_browser_type(self):

        # Used for:
        #           ordinary
        # import webbrowser as wb
        # default_browser = wb.get()
        # self.__type = default_browser.name.casefold()

        #           development
        self.__type = 'chrome'

        #           error test
        # self.__type = 'OpeRA'

    def __set_header(self, _config: dict):
        try:
            self.__header = _config[self.__type]['header']
        except KeyError:
            print(f'ERROR!\nSomething is wrong!\n Not found HEADER for {self.__type}!')
            exit(1)

    def __hide_browser_face(self):
        self.option = Options()
        self.option.add_argument(self.__header)
        self.option.add_argument('--disable-blink-features=AutomationControlled')
        self.option.add_experimental_option('detach', True)

    def __set_browser(self):
        choose_browser = {
            'firefox': webdriver.Firefox,
            'chrome': webdriver.Chrome
        }
        try:
            self.__browser = choose_browser[self.__type]()
        except selenium.common.exceptions.WebDriverException:
            print(f'ERROR!\n{self.__type}-webdriver is not founded!')
            exit(1)
        except KeyError:
            print('ERROR!\nSomething is wrong!\nUnknow browser type!')
            exit(1)

    def check_ready_to_update(self) -> bool:
        return True

    def take_screenshoot(self, img_path: str = '~/Pictures/image_for_save.png'):
        begin_name_part = 'scrnsht_'
        middle_name_part = datetime.utcnow()
        end_name_part = '_.png'
        img_name = '_'.join(str(middle_name_part).split())

        file_name = Path(img_path, begin_name_part + img_name + end_name_part)
        self.__browser.save_screenshot(str(file_name))

    def open_page(self, url_: str):
        self.__browser.get(url_)

    def get_element_from_page(self, labels_: str):
        return self.__browser.find_element(By.XPATH, labels_)

    def action_on_page(self, this_step: dict):
        elem = ''
        print('action_on_page')
        print(f'{this_step=}')
        if this_step['url']:
            print("this_step['url']")
            self.open_page(this_step['url'])
            sleep(randint(1, 3))
        if this_step['xpath']:
            print("this_step['xpath']")
            elem = self.get_element_from_page(this_step['xpath'])
            sleep(randint(1, 3))
        if elem:
            if this_step['data'] == 'Keys.RETURN':
                print("this_step['data']")
                elem.send_keys(Keys.RETURN)
            elif this_step['data']:
                print("this_step['data']")
                elem.send_keys(this_step['data'])
        sleep(randint(1, 3))


if __name__ == '__main__':
    print('This is not executable module!')
