#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Advent of Code 2020 day 4 module."""


def _hgt(x):
    if x.endswith("cm"):
        return 150 <= int(x[:-2]) <= 193
    if x.endswith("in"):
        return 59 <= int(x[:-2]) <= 76
    return False


def _hcl(x):
    if len(x) == 7 and x[0] == "#":
        int(x[1:], 16)
        return True
    return False


VALIDATORS = {
    "byr": lambda x: len(x) == 4 and 1920 <= int(x) <= 2002,
    "iyr": lambda x: len(x) == 4 and 2010 <= int(x) <= 2020,
    "eyr": lambda x: len(x) == 4 and 2020 <= int(x) <= 2030,
    "hgt": _hgt,
    "hcl": _hcl,
    "ecl": lambda x: x in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"},
    "pid": lambda x: len(x) == 9 and x.isdigit(),
    "cid": lambda x: True,
}

REQUIRED = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}


def parse_passports(puzzle_input):
    fields = []
    for line in puzzle_input:
        if line:
            fields.extend(line.split())
        else:
            yield dict((f.split(":") for f in fields))
            fields.clear()


def is_valid(passport, validate_fields=False):
    required = not REQUIRED.difference(passport)
    if not validate_fields:
        return required

    try:
        return required and all((VALIDATORS[k](v) for k, v in passport.items()))
    except ValueError:
        pass
    return False


def process(puzzle_input, verbose=False):
    passports = list(parse_passports(puzzle_input))
    p1 = sum((is_valid(p) for p in passports))
    p2 = sum((is_valid(p, True) for p in passports))
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
