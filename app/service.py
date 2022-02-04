from random import randint
from time import sleep
from typing import Dict

# from app import Browser, Config


class Service:
    def __init__(self):
        self._img_path: Dict = {
            'test_img': f'~/Pictures/some_.png',
        }

    def run(self, config_, browser_):
        for step in config_.steps:
            print(f'{step=}')
            browser_.action_on_page(step)
            sleep(randint(1, 5))
            browser_.take_screenshoot()

    def quit(self):
        pass


if __name__ == '__main__':
    print('This is not executable module!')
