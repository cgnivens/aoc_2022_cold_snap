from pathlib import Path
from .day1 import main as day1

# set the directory off of this filepath specifically
DATA_DIR = Path(__file__).absolute().parent.parent / 'data'


def main():
    print('Running Day 1')
    print('-'*20)
    day1(DATA_DIR / 'day1_input.txt')
    print('\n'*2)
