from random import randint
from time import sleep
from typing import Dict
# from configparser import ConfigParser
import configparser
import app


class Service:
    def __init__(self, _config: str):
        parser = configparser.ConfigParser()
        parser.read(_config)
        self.__config = app.Config(parser['PATH'])
        print(f'{self.__config.steps=}')
        self.__browser = app.Browser(self.__config.browser)

    def run(self):
        for step in self.__config.steps:
            print(f'{step=}')
            self.__browser.action_on_page(step)
            sleep(randint(1, 5))
            self.__browser.take_screenshoot(self.__config.img)

    def quit(self):
        pass


if __name__ == '__main__':
    print('This is not executable module!')
