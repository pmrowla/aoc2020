#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Advent of Code 2020 day 5 module."""

import itertools


def parse_seat(s):
    row = 0
    num_rows = 128
    col = 0
    num_cols = 8
    for c in s:
        if c == "F":
            num_rows = (row + num_rows) // 2
        elif c == "B":
            row = (row + num_rows) // 2
        elif c == "L":
            num_cols = (col + num_cols) // 2
        elif c == "R":
            col = (col + num_cols) // 2
    return row * 8 + col


def find_seat(empty):
    for s in empty:
        if (s + 1) not in empty and (s - 1) not in empty:
            return s


def process(puzzle_input, verbose=False):
    seats = {parse_seat(line) for line in puzzle_input}
    empty = set(range(1024)) - seats
    p1 = max(seats)
    p2 = find_seat(empty)
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
