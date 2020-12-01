#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Advent of Code 2020 day 1 module."""

from itertools import combinations
from math import prod


def product(l, r=2):
    for c in combinations(l, r):
        if sum(c) == 2020:
            return prod(c)
    raise ValueError("invalid input")


def process(puzzle_input, verbose=False):
    p1 = product(puzzle_input)
    p2 = product(puzzle_input, 3)
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
        puzzle_input = [int(line.strip()) for line in fileinput.input(args.infile)]
        p1, p2 = process(puzzle_input, verbose=args.verbose)
        print(f'Part one: {p1}')
        print(f'Part two: {p2}')
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
