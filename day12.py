#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Advent of Code 2020 day 12 module."""


def _rotate(pos, deg):
    x, y = pos
    rot = deg // 90 % 4
    return [
        (x, y),
        (y, -x),
        (-x, -y),
        (-y, x),
    ][rot]


def move(instructions, use_waypoint=False):
    pos = 0, 0
    waypoint = (10, 1) if use_waypoint else (1, 0)

    moves = {
        "N": lambda p, x: (p[0], p[1] + x),
        "S": lambda p, x: (p[0], p[1] - x),
        "E": lambda p, x: (p[0] + x, p[1]),
        "W": lambda p, x: (p[0] - x, p[1]),
    }
    rotations = {
        "L": lambda x: _rotate(waypoint, -x),
        "R": lambda x: _rotate(waypoint, x),
    }

    for inst in instructions:
        action = inst[0]
        val = int(inst[1:])
        if action in moves:
            if use_waypoint:
                waypoint = moves[action](waypoint, val)
            else:
                pos = moves[action](pos, val)
        elif action in rotations:
            waypoint = rotations[action](val)
        elif action == "F":
            pos = pos[0] + waypoint[0] * val, pos[1] + waypoint[1] * val
        else:
            raise ValueError

    return pos


def process(puzzle_input, verbose=False):
    p1 = p2 = None
    p1 = sum(map(abs, move(puzzle_input)))
    p2 = sum(map(abs, move(puzzle_input, True)))
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
