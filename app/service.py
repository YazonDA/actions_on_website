from random import randint
from time import sleep
import configparser
import app


class Service:
    def __init__(self, _config: str):
        parser = configparser.ConfigParser()
        parser.read(_config)
        self.__config = app.Config(parser['SETUP'])
        # print(f'{self.__config.steps=}')
        self.__browser = ''

    def run(self):
        # The loop for the chain-running task
        for delay in self.__config.schedule:
            print(f'This attempt will start after {delay} sec. Please wait.')
            self.make_delay(delay)
            self.__browser = app.Browser(self.__config.browser)
            for step in self.__config.steps:
                # print(f'{step=}')
                self.__browser.action_on_page(step)
                self.__browser.take_screenshoot(self.__config.img)
                # human imitation delay
                sleep(randint(1, 5))
            del self.__browser

    def make_delay(self, delay):
        sleep(delay)

    def quit(self):
        pass


if __name__ == '__main__':
    print('This is not executable module!')
