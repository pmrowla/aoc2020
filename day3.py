#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Advent of Code 2020 day 3 module."""


def traverse(grid, slope=(3, 1)):
    count = 0
    x, y = (0, 0)
    while y < len(grid) - 1:
        x = (x + slope[0]) % len(grid[0])
        y += slope[1]
        if grid[y][x] == "#":
            count += 1
    return count


def process(puzzle_input, verbose=False):
    p1 = traverse(puzzle_input)
    p2 = p1
    for slope in [(1, 1), (5, 1), (7, 1), (1, 2)]:
        p2 *= traverse(puzzle_input, slope)
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
