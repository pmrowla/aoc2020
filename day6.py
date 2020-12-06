#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Advent of Code 2020 day 6 module."""


def parse_groups(puzzle_input, intersect=False):
    group = None
    for line in puzzle_input:
        if line:
            if group is None:
                group = set(line)
            elif intersect:
                group.intersection_update(line)
            else:
                group.update(line)
        else:
            yield group
            group = None
    if group:
        yield group


def process(puzzle_input, verbose=False):
    p1 = sum([len(group) for group in parse_groups(puzzle_input)])
    p2 = sum([len(group) for group in parse_groups(puzzle_input, True)])
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
        puzzle_input = [line.strip() for line in fileinput.input(args.infile)]
        p1, p2 = process(puzzle_input, verbose=args.verbose)
        print(f'Part one: {p1}')
        print(f'Part two: {p2}')
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
