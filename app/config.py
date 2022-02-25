from pathlib import Path

from yaml import load
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper


class Config:

    def __init__(self, _config):
        app_dir = Path(__file__).resolve().parent.parent
        home_dir = Path.home()

        self.__set_steps(app_dir, _config)
        self.__set_browser_config(app_dir, _config)
        self.__set_img_path(home_dir, _config)

        self.__set_schedule(_config)

        # do it later:
        #  - place in STEPS.yaml special Keys (Secret.LOGIN and Secret.PASSWORD)
        #  - some input (implicit) Value of Login & Password
        #  - in app find&replace Keys to Value
        # self.secret_path = _config['SECRET_CONFIG']

    def __set_steps(self, app_dir, _config):
        steps_path = Path(app_dir, _config['STEPS_CONFIG'])
        with open(steps_path, "r") as file_:
            self.steps = load(file_, Loader=Loader)

    def __set_browser_config(self, app_dir, _config):
        browser_config_path = Path(app_dir, _config['BROWSER_CONFIG'])
        with open(browser_config_path, "r") as file_:
            self.browser = load(file_, Loader=Loader)

    def __set_img_path(self, home_dir, _config):
        img_path = Path(home_dir, _config['IMG_CONFIG'])
        if not img_path.exists():
            img_path.mkdir()
        self.img = img_path

    def __set_schedule(self, _config):
        self.schedule = schedule_parser(_config['START_TIMES'])


def schedule_parser(time_list: str) -> tuple:
    """ Module translate string-list of the hours/minutes to the tuple of the seconds.
    :arg
    string like "hh:mm; hh:mm".
    mm & hh must be greater Zero.
    separate between hh & mm must be ':'.
    separate between some hh:mm must be ';'.
    :return
    tuple like (60, 13860)
    """
    tmp_list = []
    try:
        time_list = time_list.split('; ')
    except ValueError as e:
        # print(f'Wrong format or empty time_list. Will return (0,).')
        return tuple(0,)
    for time_ in time_list:
        try:
            sec_ = time_.split(':')
            tmp_time_1 = int(sec_[0])*3600
            tmp_time_2 = int(sec_[1])*60 if len(sec_) > 1 else 0
            if tmp_time_1 < 0 or tmp_time_2 < 0:
                raise ValueError
            else:
                sec_ = tmp_time_1 + tmp_time_2
        except ValueError as e:
            # print(f'The "{time_}" in ({time_list}) is a wrong format. Will set 0.')
            sec_ = 0
        tmp_list.append(sec_)
    return tuple(tmp_list)


if __name__ == '__main__':
    print('This is not executable module!')
