#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Advent of Code 2020 day 18 module."""


class Expr:

    OPS = {
        "+": lambda l, r: l + r,
        "*": lambda l, r: l * r,
    }

    def __init__(self, tokens):
        self.tokens = tokens

    def __str__(self):
        return "({})".format(" ".join([str(t) for t in self.tokens]))

    def eval(self):
        if not self.tokens:
            raise ValueError("Empty expression")

        result = None
        next_op = None
        for t in self.tokens:
            if hasattr(t, "eval"):
                t = t.eval()
            if isinstance(t, int):
                if next_op is None:
                    result = t
                else:
                    result = self.OPS[next_op](result, t)
                    next_op = None
            else:
                next_op = t
        return result


    @classmethod
    def from_string(cls, s):
        tokens = []
        start = 0
        while start < len(s):
            c = s[start]
            if c.isdigit():
                end = start + 1
                while end < len(s) and s[end].isdigit():
                    end += 1
                tokens.append(int(s[start:end]))
                start = end - 1
            elif c == "(":
                depth = 1
                end = start + 1
                while end < len(s):
                    if s[end] == ")":
                        depth -= 1
                        if depth == 0:
                            break
                    elif s[end] == "(":
                        depth += 1
                    end += 1
                if end >= len(s):
                    raise ValueError(f"Unmatched parentheses at {start}")
                tokens.append(cls.from_string(s[start+1 : end]))
                start = end
            elif c in "+*":
                tokens.append(c)
            start += 1
        return cls(tokens)


class Expr2(Expr):

    def eval(self):
        if not self.tokens:
            raise ValueError("Empty expression")

        tokens = [t.eval() if hasattr(t, "eval") else t for t in self.tokens]
        for op in ("+", "*"):
            if len(tokens) == 1:
                break
            reduced = []
            next_op = None
            l = None
            for t in tokens:
                if isinstance(t, int):
                    if next_op is None:
                        l = t
                        reduced.append(l)
                    else:
                        l = self.OPS[next_op](l, t)
                        reduced[-1] = l
                        next_op = None
                else:
                    if t == op:
                        next_op = t
                    else:
                        reduced.append(t)
            tokens = reduced
        return tokens[0]


def process(puzzle_input, verbose=False):
    p1 = sum(Expr.from_string(line).eval() for line in puzzle_input)
    p2 = sum(Expr2.from_string(line).eval() for line in puzzle_input)
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
