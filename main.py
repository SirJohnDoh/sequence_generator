#!env/bin/python

import argparse

from generator import Generator

from fibinacci import Fibinacci


def main():
    fib = Fibinacci()
    parser = argparse.ArgumentParser(
        description=(
            'Find method of representing a number given sums of numbers from a sequnce.'
            'Or a list of every representation up to the given number.'
        )
    )
    parser.add_argument(
        'integer',
        metavar='n',
        type=int,
        help='Integer to represent or maximum value of multiple representations'
    )
    parser.add_argument(
        '--sequence_list',
        dest='function',
        action='store_const',
        help='Find representation of every number up till the given integer',
        const=fib.get_every_sum_solution_up_to,
        default=fib.get_sum_solution_for,
    )
    parser.add_argument(
        '--quiet',
        action='store_true',
    )
    args = parser.parse_args()
    solution = args.function(args.integer)
    if args.quiet:
        return
    if isinstance(solution, list):
        for sol in solution:
            print(sol[0])
    else:
        print(solution)


if __name__=="__main__":
    main()
