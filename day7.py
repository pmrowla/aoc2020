#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Advent of Code 2020 day 7 module."""

import re


def bag_color(bag):
    return bag.strip().rsplit(maxsplit=1)[0]


def parse_rule(line):
    parent, children = line.split("contain")
    parent_color = bag_color(parent)
    child_colors = []
    if children.strip().startswith("no other"):
        return {parent_color: {}}
    child_bags = {}
    for child in children.rstrip(".").split(","):
        num, bag = child.split(maxsplit=1)
        num = int(num)
        child_bags[bag_color(bag)] = num
    return {parent_color: child_bags}


def possible_parents(parents, rules, color):
    for parent_color, children in rules.items():
        if parent_color in parents:
            continue
        if color in children:
            parents.add(parent_color)
            possible_parents(parents, rules, parent_color)


def count_children(color, rules):
    count = 0
    for child_color, child_count in rules[color].items():
        count += child_count * count_children(child_color, rules)
        count += child_count
    return count


def process(puzzle_input, verbose=False):
    rules = {}
    for line in puzzle_input:
        rules.update(parse_rule(line))
    parents = set()
    possible_parents(parents, rules, "shiny gold")
    p1 = len(parents)
    p2 = count_children("shiny gold", rules)
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
