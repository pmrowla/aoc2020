#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Advent of Code 2020 day 22 module."""

from collections import deque
from itertools import islice


def turn(deck1, deck2):
    card1 = deck1.popleft()
    card2 = deck2.popleft()
    if card1 > card2:
        deck1.extend([card1, card2])
    else:
        deck2.extend([card2, card1])


def recursive_game(deck1, deck2):
    seen = set()

    while deck1 and deck2:
        if (tuple(deck1), tuple(deck2)) in seen:
            return 1
        seen.add((tuple(deck1), tuple(deck2)))
        card1 = deck1.popleft()
        card2 = deck2.popleft()
        if len(deck1) >= card1 and len(deck2) >= card2:
            winner = recursive_game(deque(islice(deck1, 0, card1)), deque(islice(deck2, 0, card2)))
        elif card1 > card2:
            winner = 1
        else:
            winner = 2
        if winner == 1:
            deck1.extend([card1, card2])
        else:
            deck2.extend([card2, card1])
    return 1 if deck1 else 2


def process(puzzle_input, verbose=False):
    p1 = p2 = None

    deck1 = deque()
    deck2 = deque()

    deck = None
    for line in puzzle_input:
        if line == "Player 1:":
            deck = deck1
        elif line == "Player 2:":
            deck = deck2
        else:
            deck.append(int(line))
    recursive_deck1 = deque(deck1)
    recursive_deck2 = deque(deck2)

    while deck1 and deck2:
        turn(deck1, deck2)
    winner = deck1 if deck1 else deck2

    p1 = sum((len(winner) - i) * c for i, c in enumerate(winner))

    winner = recursive_game(recursive_deck1, recursive_deck2)
    winner = recursive_deck1 if winner == 1 else recursive_deck2
    p2 = sum((len(winner) - i) * c for i, c in enumerate(winner))

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
