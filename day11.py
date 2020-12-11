#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Advent of Code 2020 day 11 module."""

from itertools import product


def empty(grid, pos):
    x, y = pos
    return grid[y][x] == "L"


def occupied(grid, pos):
    x, y = pos
    return grid[y][x] == "#"


DELTAS = {
    "nw": (-1, -1),
    "n": (0, -1),
    "ne": (1, -1),
    "e": (1, 0),
    "se": (1, 1),
    "s": (0, 1),
    "sw": (-1, 1),
    "w": (-1, 0),
}


def adj(grid, pos, immediate=True):
    x, y = pos

    for x_delta, y_delta in DELTAS.values():
        i = 1
        while True:
            x1 = x + i * x_delta
            y1 = y + i * y_delta
            if x1 < 0 or x1 >= len(grid[y]) or y1 < 0 or y1 >= len(grid):
                break
            if immediate:
                yield x1, y1
                break
            if grid[y1][x1] != ".":
                yield x1, y1
                break
            i += 1


def step(grid, limit=4, immediate=True):
    new_grid = []
    for y in range(len(grid)):
        new_row = []
        for x in range(len(grid[y])):
            if empty(grid, (x, y)) and not any(
                occupied(grid, pos)
                for pos in adj(grid, (x, y), immediate=immediate)
            ):
                new_row.append("#")
            elif occupied(grid, (x, y)) and sum(
                occupied(grid, pos)
                for pos in adj(grid, (x, y), immediate=immediate)
            ) >= limit:
                new_row.append("L")
            else:
                new_row.append(grid[y][x])
        new_grid.append(new_row)
    return new_grid


def count_occupied(puzzle_input, **kwargs):
    grid = [list(row) for row in puzzle_input]
    next_grid = None
    while True:
        next_grid = step(grid, **kwargs)
        if next_grid == grid:
            break
        grid = next_grid
    return sum((occupied(grid, pos) for pos in product(range(len(grid[0])), range(len(grid)))))


def process(puzzle_input, verbose=False):
    p1 = count_occupied(puzzle_input)
    p2 = count_occupied(puzzle_input, limit=5, immediate=False)
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
