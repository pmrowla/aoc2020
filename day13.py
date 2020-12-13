#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Advent of Code 2020 day 13 module."""

import math


def  _earliest_time(bus, arrival):
    return math.ceil(arrival / bus) * bus


def earliest(buses, arrival):
    earliest_bus = None
    earliest_time = None
    for bus, _ in buses:
        if bus is None:
            continue
        time = _earliest_time(bus, arrival)
        if earliest_time is None or time < earliest_time:
            earliest_bus = bus
            earliest_time = time
    return earliest_bus, earliest_time


def crt(nums):
    # chinese remainder theorem
    m_prod = math.prod(a for a, _ in nums)
    return (
        sum(
            b * m_prod // a * pow(m_prod // a, -1, a)
            for a, b in nums
        ) % m_prod
    )


def process(puzzle_input, verbose=False):
    arrival = int(puzzle_input[0])
    buses = [(int(bus), i) for i, bus in enumerate(puzzle_input[1].split(",")) if bus != "x"]

    bus, time = earliest(buses, arrival)
    p1 = bus * (time - arrival)
    p2 = crt([(bus, bus - offset) for bus, offset in buses])
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
