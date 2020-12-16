#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Advent of Code 2020 day 16 module."""


def parse_rule(line):
    rule, rule_ranges = line.split(":")
    ranges = []
    for r in rule_ranges.strip().split("or"):
        ranges.append(tuple([int(n.strip()) for n in r.split("-")]))
    return {rule: ranges}


def validate(ticket, rules):
    for value in ticket:
        valid_value = False
        for _field, ranges in rules.items():
            if any(r[0] <= value <= r[1] for r in ranges):
                valid_value = True
                break
        if not valid_value:
            return False, value
    return True, None


def reduce_fields(fields):
    while True:
        done = True
        matched = [v for v in fields.values() if len(v) == 1]
        for f in fields:
            if len(fields[f]) > 1:
                fields[f].difference_update(*matched)
                done = False
        if done:
            break


def identify_fields(tickets, rules):
    fields = {}
    for t in tickets:
        ticket_len = len(t)
        break

    for field, ranges in rules.items():
        intersect = set(range(ticket_len))
        for t in tickets:
            potential = set()
            for i, value in enumerate(t):
                if any(r[0] <= value <= r[1] for r in ranges):
                    potential.add(i)
            intersect.intersection_update(potential)
        fields[field] = intersect
    reduce_fields(fields)
    return {f: v.pop() for f, v in fields.items()}


def process(puzzle_input, verbose=False):
    p1 = p2 = None
    state = 0
    rules = {}
    my_ticket = None
    nearby = set()
    for line in puzzle_input:
        if line:
            if line in ("your ticket:", "nearby tickets:"):
                continue
            if state == 0:
                rules.update(parse_rule(line))
            else:
                ticket = tuple([int(n) for n in line.split(",")])
                if state == 1:
                    my_ticket = ticket
                else:
                    nearby.add(ticket)
        else:
            state += 1

    invalid = set()
    p1 = 0
    for t in nearby:
        valid, val = validate(t, rules)
        if not valid:
            p1 += val
            invalid.add(t)
    nearby -= invalid
    fields = identify_fields(nearby, rules)

    p2 = 1
    for f, pos in fields.items():
        if f.startswith("departure"):
            p2 *= my_ticket[pos]
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
