"""
--- Day 5: Supply Stacks ---
The expedition can depart as soon as the final supplies have been unloaded from the ships. Supplies are stored in stacks of marked crates, but because the needed supplies are buried under many other crates, the crates need to be rearranged.

The ship has a giant cargo crane capable of moving crates between stacks. To ensure none of the crates get crushed or fall over, the crane operator will rearrange them in a series of carefully-planned steps. After the crates are rearranged, the desired crates will be at the top of each stack.

The Elves don't want to interrupt the crane operator during this delicate procedure, but they forgot to ask her which crate will end up where, and they want to be ready to unload them as soon as possible so they can embark.

They do, however, have a drawing of the starting stacks of crates and the rearrangement procedure (your puzzle input). For example:

    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
In this example, there are three stacks of crates. Stack 1 contains two crates: crate Z is on the bottom, and crate N is on top. Stack 2 contains three crates; from bottom to top, they are crates M, C, and D. Finally, stack 3 contains a single crate, P.

Then, the rearrangement procedure is given. In each step of the procedure, a quantity of crates is moved from one stack to a different stack. In the first step of the above rearrangement procedure, one crate is moved from stack 2 to stack 1, resulting in this configuration:

[D]        
[N] [C]    
[Z] [M] [P]
 1   2   3 
In the second step, three crates are moved from stack 1 to stack 3. Crates are moved one at a time, so the first crate to be moved (D) ends up below the second and third crates:

        [Z]
        [N]
    [C] [D]
    [M] [P]
 1   2   3
Then, both crates are moved from stack 2 to stack 1. Again, because crates are moved one at a time, crate C ends up below crate M:

        [Z]
        [N]
[M]     [D]
[C]     [P]
 1   2   3
Finally, one crate is moved from stack 1 to stack 2:

        [Z]
        [N]
        [D]
[C] [M] [P]
 1   2   3
The Elves just need to know which crate will end up on top of each stack; in this example, the top crates are C in stack 1, M in stack 2, and Z in stack 3, so you should combine these together and give the Elves the message CMZ.

"""
from itertools import groupby
import re
from collections import defaultdict, deque

def process_file(fh):
    instructions = re.compile(r"(\d)+")
    box_whitespace = re.compile(r"(\s{4}|\s{1})+")

    while True:
        line = next(fh).strip('\n')

        if not line:
            yield line
            break
        elif not '[' in line:
            continue
        
        boxes = [box.strip().replace('[', '').replace(']', '') for box in box_whitespace.split(line) if box]
        yield boxes

    for line in fh:
        yield [int(instruction) for instruction in instructions.findall(line.strip())]


def main(datafile):
    with open(datafile) as fh:
        lines = process_file(fh)
        crates, instructions = [list(grp) for k, grp in groupby(lines, key=bool) if k]

    stacks = defaultdict(deque)

    for group in zip(*crates):
        for i, item in enumerate(group, start=1):
            if not item:
                continue
            stacks[i].appendleft(item)
    
    # print(crates, instructions)
    print(stacks)


if __name__ == "__main__":
    from io import StringIO

    content = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

    with StringIO(content) as fh:
        lines = process_file(fh)
        crates, instructions = [list(grp) for k, grp in groupby(lines, key=bool) if k]

    print(crates, instructions)
    stacks = defaultdict(deque)

    for group in crates:
        for i, item in enumerate(group, start=1):
            if not item:
                continue
            stacks[i].appendleft(item)

    print(stacks)
