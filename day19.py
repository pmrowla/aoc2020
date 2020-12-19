#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Advent of Code 2020 day 19 module."""

import itertools


def parse_rule(line):
    key, line = line.split(":")
    line = line.strip()
    if '"' in line:
        value = line.strip('"')
    else:
        value = [tuple(int(k) for k in rule.strip().split()) for rule in line.strip().split("|")]
    return {int(key): value}


def eval_rule(rules, key):
    if isinstance(rules[key], str):
        return rules[key]
    matches = []
    for case in rules[key]:
        substrings = []
        for subkey in case:
            if subkey == key:
                raise ValueError("cannot eval loop")
            sub_match = eval_rule(rules, subkey)
            if isinstance(sub_match, str):
                substrings.append((sub_match,))
            else:
                substrings.append(sub_match)
        matches.extend(["".join(s) for s in itertools.product(*substrings)])
    return set(matches)


def count_valid_loop(rules, messages):
    # 0 is always "0: 8 11" and is always the only rule containing either 8 or 11
    # To validate a message we need to check if m matches:
    #   42 [42...] 42 [(42 31)...] 31
    # Simplified, you get 42... 31... where the number of 42's must be at least
    # one more than the number of 31's

    valid_42 = eval_rule(rules, 42)
    for s in valid_42:
        len_42 = len(s)
        break

    valid_31 = eval_rule(rules, 31)
    for s in valid_42:
        len_31 = len(s)
        break

    def is_valid(msg):
        start = 0
        if msg[:len_42] not in valid_42:
            return False
        count_42 = 1
        while msg[start : start+len_42] in valid_42:
            start += len_42
        end_42 = start
        count_42 = end_42 // len_42

        if msg[start : start+len_31] not in valid_31:
            return False
        start += len_31
        while msg[start : start+len_31] in valid_31:
            start += len_31
        if msg[start:]:
            return False
        count_31 = (start - end_42) // len_31
        return count_42 > count_31

    count = 0
    for m in messages:
        if is_valid(m):
            count += 1
    return sum(is_valid(m) for m in messages)


def process(puzzle_input, verbose=False):
    p1 = p2 = None
    parsing_rules = True
    rules = {}
    messages = set()
    for line in puzzle_input:
        if not line:
            parsing_rules = False
            continue
        if parsing_rules:
            rules.update(parse_rule(line))
        else:
            messages.add(line)

    valid = eval_rule(rules, 0)
    p1 = len(valid & messages)
    p2 = count_valid_loop(rules, messages)

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
