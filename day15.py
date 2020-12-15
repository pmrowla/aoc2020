#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Advent of Code 2020 day 15 module."""

try:
    from tqdm import tqdm

    HAS_TQDM = True
except ImportError:
    HAS_TQDM = False


def run(start):
    numbers = {}
    turn = 0
    for n in start:
        yield n
        numbers[n] = (None, turn)
        turn += 1
    next_ = 0

    while True:
        yield next_
        if next_ in numbers:
            new = (numbers[next_][1], turn)
            numbers[next_] = new
            next_ = new[1] - new[0]
        else:
            numbers[next_] = (None, turn)
            next_ = 0
        turn += 1


def process(puzzle_input, verbose=False):
    p1 = p2 = None
    nums = run([int(n) for n in puzzle_input[0].split(",")])

    if HAS_TQDM:
        r = tqdm(range(30000000))
    else:
        r = range(30000000)
    for i in r:
        n = next(nums)
        if i == 2019:
            p1 = n
    p2 = n
    return p1, p2


def main():
    """Main entry point."""
    import argparse
    import fileinput

    parser = argparse.ArgumentParser()
    parser.add_argument('infile', help='input file to read ("-" for stdin)')
    parser.add_argument('-v', '--verbose', '-d', '--debug',
                        action='store_true', dest='verbose', help='verbose output')
    args = parser.parse_args()
    try:
        puzzle_input = [line.strip() for line in fileinput.input(args.infile) if line.strip()]
        p1, p2 = process(puzzle_input, verbose=args.verbose)
        print(f'Part one: {p1}')
        print(f'Part two: {p2}')
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
