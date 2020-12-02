#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Advent of Code 2020 day 2 module."""


def is_valid(line):
    policy, password = line.split(":")
    n, c = policy.split()
    min_, max_ = map(int, n.split("-"))
    password = password.strip()
    count = list(password).count(c)
    return (
        count >= min_ and count <= max_,
        list(password[min_ - 1] + password[max_ - 1]).count(c) == 1
    )


def process(puzzle_input, verbose=False):
    return map(sum, zip(*[is_valid(line) for line in puzzle_input]))


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
