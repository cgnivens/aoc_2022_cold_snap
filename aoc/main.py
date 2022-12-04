from pathlib import Path
from .day1 import main as day1
from .day2 import main as day2
from .day3 import main as day3

# set the directory off of this filepath specifically
DATA_DIR = Path(__file__).absolute().parent.parent / 'data'


def main():
    print('Running Day 1')
    print('-'*20)
    day1(DATA_DIR / 'day1_input.txt')
    print('\n'*2)

    print('Running Day 2')
    print('-'*20)
    day2(DATA_DIR / 'day2_input.txt')
    print('\n'*2)

    print('Running Day 3')
    print('-'*20)
    day3(DATA_DIR / 'day3_input.txt')
