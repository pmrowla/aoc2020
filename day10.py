#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Advent of Code 2020 day 10 module."""

import math
from collections import defaultdict


def process(puzzle_input, verbose=False):
    adapters = [0] + list(sorted(puzzle_input)) + [max(puzzle_input) + 3]
    required = {0, adapters[-1]}
    counts = defaultdict(int)

    # number of ways consecutive runs w/diff of 1 can be arranged
    combinations = []
    run_len = 0
    for i in range(len(adapters) - 1):
        diff = adapters[i + 1] - adapters[i]
        counts[diff] += 1
        if diff == 1:
            run_len += 1
        else:
            if run_len > 0:
                comb = sum(
                    (
                        math.comb(run_len - 1, x)
                        for x in range(max(run_len - 3, 0), run_len + 1)
                    )
                )
                combinations.append(comb)
            run_len = 0
    p1 = counts[1] * counts[3]

    prod = 1
    p2 = math.prod(combinations)
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
        puzzle_input = [int(line.strip()) for line in fileinput.input(args.infile) if line.strip()]
        p1, p2 = process(puzzle_input, verbose=args.verbose)
        print(f'Part one: {p1}')
        print(f'Part two: {p2}')
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
