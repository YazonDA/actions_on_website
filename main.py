import sys
from app import Browser, Service, Config


def main(*args):
    browser = Browser()
    service = Service()
    config = Config()
    service.run(config, browser)
    print(f'OK')


if __name__ == '__main__':
    sys.exit(main(sys.argv))
