#!/usr/bin/env python3

import click
import importlib

@click.command()
@click.argument('day')
def solve(day: str):
    if day == 'all':
        for i in range(1, 25):
            solve_day(i)
    else:
        solve_day(day)

def solve_day(daynum):
    click.echo(f"--- Day {daynum} ---")

    with open(f'inputs/day{daynum}.txt') as file:
        input = file.read()

    day = importlib.import_module(f'day{daynum}')

    click.echo(f"First part  : {get_output(day, 'first',  input)}")
    click.echo(f"Second part : {get_output(day, 'second', input)}")

def get_output(module, func, input):
    try:
        return getattr(module, func)(input)
    except:
        return click.style("(Not implemented)", italic=True)

if __name__ == '__main__':
    solve()
