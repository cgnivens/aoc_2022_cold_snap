from pathlib import Path
from .day1 import main as day1

DATA_DIR = Path('.').absolute() / 'data'


def main():
    print('Running Day 1')
    print('-'*20)
    day1(DATA_DIR / 'day1_input.txt')
    print('\n'*2)
