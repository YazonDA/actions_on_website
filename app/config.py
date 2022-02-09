from pathlib import Path

from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper


class Config:

    def __init__(self, _config):
        app_dir = Path(__file__).resolve().parent.parent
        steps_path = Path(app_dir, _config['STEPS_CONFIG'])
        self.__set_steps(steps_path)
        browser_config_path = Path(app_dir, _config['BROWSER_CONFIG'])
        self.__set_browser_config(browser_config_path)
        self.__set_img_path(_config['IMG_CONFIG'])

        self.secret_path = _config['SECRET_CONFIG']

    def __set_steps(self, steps_path):
        with open(steps_path, "r") as file_:
            self.steps = load(file_, Loader=Loader)

    def __set_browser_config(self, browser_path):
        with open(browser_path, "r") as file_:
            self.browser = load(file_, Loader=Loader)

    def __set_img_path(self, img_path):
        home_dir = Path.home()
        img_path = Path(home_dir, img_path)
        if not img_path.exists():
            img_path.mkdir()
        self.img = img_path


if __name__ == '__main__':
    print('This is not executable module!')
