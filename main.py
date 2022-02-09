import sys
from app import Service


def main(*args):
    config = 'setup.ini'
    service = Service(config)
    service.run()
    print(f'OK')


if __name__ == '__main__':
    sys.exit(main(sys.argv))
