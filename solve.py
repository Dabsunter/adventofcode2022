#!/usr/bin/env python3

import click
import importlib

NOT_IMPLEMENTED = click.style("(Not implemented)", italic=True)

@click.command()
@click.argument('day')
def solve(day: str):
    try:
        if day == 'all':
                for i in range(1, 26):
                    solve_day(i)
        else:
            solve_day(day)
    except FileNotFoundError:
        click.echo(NOT_IMPLEMENTED)

def solve_day(daynum):
    click.echo(click.style(f"--- Day {daynum} ---", bold=True))

    with open(f'inputs/day{daynum}.txt') as file:
        input = file.read()

    day = importlib.import_module(f'day{daynum}')

    click.echo(f"First part  : {get_output(day, 'part1', input)}")
    click.echo(f"Second part : {get_output(day, 'part2', input)}")

def get_output(module, func, input):
    if (part := getattr(module, func, False)):
        return part(input)
    return NOT_IMPLEMENTED

if __name__ == '__main__':
    solve()
