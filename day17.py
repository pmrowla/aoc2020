#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Advent of Code 2020 day 17 module."""

import itertools
from collections import defaultdict

try:
    from tqdm import tqdm

    HAS_TQDM = True
except ImportError:
    HAS_TQDM = False


def adj(pos, dimensions):
    for delta in itertools.product(tuple(range(-1, 2, 1)), repeat=dimensions):
        if delta == (0,) * dimensions:
            continue
        yield tuple(
            pos[i] + delta[i]
            for i in range(dimensions)
        )


def step(grid, dimensions, mins, maxes):
    new_grid = defaultdict(bool)
    dim_ranges = [
        range(mins[d] - 1, maxes[d] + 2, 1)
        for d in range(dimensions)
    ]
    positions = list(itertools.product(*dim_ranges))
    if HAS_TQDM:
        positions = tqdm(positions, desc="Check neighbors", leave=False)
    for pos in positions:
        active_neighbors = sum(grid[neighbor] for neighbor in adj(pos, dimensions))
        if grid[pos]:
            new_grid[pos] = 2 <= active_neighbors <= 3
        else:
            new_grid[pos] = active_neighbors == 3
    return new_grid, tuple(n - 1 for n in mins), tuple(n + 1 for n in maxes)


def parse_grid(puzzle_input, dimensions):
    grid = defaultdict(bool)
    extra = (0,) * (dimensions - 2)
    for y, row in enumerate(puzzle_input):
        for x, c in enumerate(row):
            grid[(x, y) + extra] = c == "#"
    return grid, len(puzzle_input[0]), len(puzzle_input)


def run(puzzle_input, dimensions=3):
    grid, max_x, max_y = parse_grid(puzzle_input, dimensions)
    mins = (0,) * dimensions
    maxes = (max_x, max_y) + (0,) * dimensions

    if HAS_TQDM:
        r = tqdm(range(6), desc=f"Part {dimensions - 2}")
    else:
        r = range(6)
    for _ in r:
        grid, mins, maxes = step(grid, dimensions, mins, maxes)
    return sum(grid.values())
    

def process(puzzle_input, verbose=False):
    p1 = run(puzzle_input)
    p2 = run(puzzle_input, 4)
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
