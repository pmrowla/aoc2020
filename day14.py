#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Advent of Code 2020 day 14 module."""

import itertools
import re

class Emulator:
    MEM_RE = re.compile(r"mem\[(?P<addr>\d+)\] = (?P<val>\d+)")

    def __init__(self):
        self._reset()

    def _reset(self):
        self.and_mask = 0
        self.or_mask = 0
        self.mem_floating_bits = []
        self.mem = {}

    def set_mask(self, line, **kwargs):
        _, mask = line.split("=")
        mask = mask.strip()
        and_mask = 0
        or_mask = 0
        floating_bits = []
        for i, c in enumerate(mask):
            bit = len(mask) - 1 - i
            if c == "1":
                or_mask |= 1 << bit
            if c != "0":
                and_mask |= 1 << bit
            if c == "X":
                floating_bits.append(bit)
        self.and_mask = and_mask
        self.or_mask = or_mask
        self.mem_floating_bits = floating_bits

    def set_mem(self, line, v2=False):
        m = self.MEM_RE.match(line)
        addr = int(m.group("addr"))
        val = int(m.group("val"))
        if v2:
            addr |= self.or_mask
            for bit_vals in itertools.product(
                range(2), repeat=len(self.mem_floating_bits)
            ):
                vaddr = addr
                for i in range(len(bit_vals)):
                    mask = 1 << self.mem_floating_bits[i]
                    if bit_vals[i] == 1:
                        vaddr |= mask
                    else:
                        vaddr &= ((1 << 36) - 1) - mask
                self.mem[vaddr] = val
        else:
            self.mem[addr] = val & self.and_mask | self.or_mask

    def run(self, prog, **kwargs):
        self._reset()
        for line in prog:
            if line.startswith("mask"):
                self.set_mask(line, **kwargs)
            elif line.startswith("mem"):
                self.set_mem(line, **kwargs)


def process(puzzle_input, verbose=False):
    emu = Emulator()
    emu.run(puzzle_input)
    p1 = sum(emu.mem.values())
    emu.run(puzzle_input, v2=True)
    p2 = sum(emu.mem.values())
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
