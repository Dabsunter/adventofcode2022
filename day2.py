import itertools

opponent_plays = "ABC"
our_plays      = "XYZ"

draws  = set(zip(opponent_plays, our_plays))
wins   = set(zip(opponent_plays, (2*our_plays)[1:]))
looses = set(zip((2*opponent_plays)[1:], our_plays))

def calc_score(opponent_play, our_play):
    if (opponent_play, our_play) in wins:
        score = 6
    elif (opponent_play, our_play) in draws:
        score = 3
    elif (opponent_play, our_play) in looses:
        score = 0
    else:
        raise Exception("WTF ?")

    return score + our_plays.index(our_play) + 1

def part1(input: str):
    return sum(calc_score(*line.split()) for line in input.splitlines())

guess = {(k, 'X'): v for k,v in looses}
guess.update({(k, 'Y'): v for k,v in draws})
guess.update({(k, 'Z'): v for k,v in wins})

def part2(input: str):
    return sum(calc_score(opp, guess[opp,our]) for opp,our in map(str.split, input.splitlines()))
