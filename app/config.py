import os
from os import path
from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper


def _dotenv():
    from dotenv import load_dotenv
    dotenv_path = path.join(path.dirname(__file__), '.env')
    if path.exists(dotenv_path):
        load_dotenv(dotenv_path)


class Config(object):

    def __init__(self):
        _dotenv()
        target_config = os.environ.get('TARGET_CONFIG') or 'you_will_never_find'
        with open(target_config, "r") as file_:
            self.steps = load(file_, Loader=Loader)
        print(f'{self.steps=}')


if __name__ == '__main__':
    print('This is not executable module!')
