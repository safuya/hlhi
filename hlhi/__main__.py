import argparse
from datetime import datetime
from hlhi import time_difference


def date(string):
    try:
        return datetime.strptime(string, '%Y-%m-%d')
    except ValueError:
        raise argparse.ArgumentTypeError('The date must be in the format YYYY-MM-DD')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Tools for books.')
    parser.add_argument('--bought', '-b', action='store', type=date)
    parser.add_argument('--sold', '-s', action='store', type=date, default=datetime.now())
    args = parser.parse_args()
    print(str(time_difference.run(args.bought, args.sold)))
