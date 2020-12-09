#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Advent of Code 2020 day 9 module."""
from bisect import bisect_left


def validate(nums, n):
    last = list(sorted(nums))
    index = bisect_left(last, n)
    for i in range(index - 1, -1, -1):
        for j in range(i - 1, -1, -1):
            if last[i] + last[j] == n:
                return True
    return False


def weakness(nums, n):
    for i in range(len(nums)):
        if nums[i] >= n:
            continue
        for j in range(i + 1, len(nums)):
            l = nums[i:j+1]
            if sum(l) == n:
                return min(l) + max(l)


def process(puzzle_input, verbose=False):
    preamble = 25
    nums = puzzle_input[:preamble]
    for n in puzzle_input[preamble:]:
        if validate(nums[-preamble:], n):
            nums.append(n)
        else:
            p1 = n
            break

    p2 = weakness(puzzle_input, p1)
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
