from pathlib import Path
from .day1 import main as day1
from .day2 import main as day2
from .day3 import main as day3
from .day4 import main as day4
from .day5 import main as day5
from .day6 import main as day6
from .day7 import main as day7
from .day8 import main as day8

# set the directory off of this filepath specifically
DATA_DIR = Path(__file__).absolute().parent.parent / 'data'


def main():
    funcs = (
        day1,
        day2,
        day3,
        day4,
        day5,
        day6,
        day7,
        day8,
    )

    for i, func in enumerate(funcs, start=1):
        print(f"Running Day {i}")
        print('-'*20)
        func(DATA_DIR / f'day{i}_input.txt')
        print('\n'*2)
