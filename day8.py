#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Advent of Code 2020 day 8 module."""


class CPU:
    def __init__(self):
        self.acc = 0
        self.pc = 0

    def _acc(self, x):
        self.acc += x
        return 1

    def _jmp(self, x):
        return x

    def _nop(self, x):
        return 1

    def run(self, prog):
        self.acc = 0
        self.pc = 0
        executed = set()
        while self.pc < len(prog):
            if self.pc in executed:
                return None
            executed.add(self.pc)
            opcode, val = prog[self.pc]
            op = getattr(self, f"_{opcode}")
            self.pc += op(int(val))
        return self.acc


def process(puzzle_input, verbose=False):
    cpu = CPU()
    prog = [line.split() for line in puzzle_input]

    cpu.run(prog)
    p1 = cpu.acc

    swap = {
        "jmp": "nop",
        "nop": "jmp",
    }
    for i, (opcode, val) in enumerate(prog):
        if opcode in swap:
            p2 = cpu.run(prog[:i] + [(swap[opcode], val)] + prog[i + 1:])
            if p2 is not None:
                break

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
