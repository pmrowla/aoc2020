#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Advent of Code 2020 day 21 module."""

from collections import Counter


def parse(line):
    ing_s, all_s= line.split("(contains ")
    ingredients = set(ing_s.strip().split())
    allergens = {s.strip(): ingredients for s in all_s.strip(")").split(",")}
    return ingredients, allergens


def find_allergens(possible_allergens):
    allergens = {}
    while possible_allergens:
        to_remove = None
        for k, v in possible_allergens.items():
            v.difference_update(allergens.values())
            if len(v) == 1:
                allergens[k] = v.pop()
                del possible_allergens[k]
                break
    return allergens


def process(puzzle_input, verbose=False):
    p1 = p2 = None

    ingredients = Counter()
    possible_allergens = {}

    eggs = []
    for line in puzzle_input:
        i, a = parse(line)
        ingredients.update(i)
        for k, v in a.items():
            if k in possible_allergens:
                possible_allergens[k].intersection_update(v)
            else:
                possible_allergens[k] = set(v)
    non_allergens = set(ingredients).difference(*possible_allergens.values())
    p1 = sum(ingredients[i] for i in non_allergens)
    allergens = find_allergens(possible_allergens)
    p2 = ",".join(allergens[k] for k in sorted(allergens))
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
