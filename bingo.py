"""
TODO:
    Implement Matplotlib on VSC so I can test in real time
    Figure out how to display multiple histograms on the same axes
    Create biased draw methods
    And probably some more stuff I forgot how to do before.
"""

from random import choice, getrandbits, randint
import matplotlib.pyplot as plt

def draw(biased):
    # assumption: biased is boolean or 0 & 1
    if bloated:
        return # return random_draw()
    elif random:
        draw_number = randint(1,36)
        roll_record.append(draw_number)
        return draw_number
    else:
        print("You messed up somewhere!")


def play_bingo(type):
    # For many rounds of bingo, lines are of no use to us.
    # Only (36-N) unique draws and (N * 10) dupes
    board = 0
    dupe_count = 0
    draw_record = []
    # Or board, dupe_count, draw_record = 0, 0, []
    while board < 36:
        draws += 1
        if draw(type) in draw_record:
            dupe_count += 1
        else:
            board += 1
        if board + math.floor(dupe_count/10) == 36:
            print("Bingo fully cleared!")
        return draws
        
def bingo_sim(samples, type):
    draw_count = []
    for i in range(samples):
        draw_count.append(play_bingo(type))
    x = list(range(50,105))
    plt.hist(draw_count, bins = x)

# Until I figure out how to do this bit...
if __name__ == "__main__:
    x = list(range(50,105))
    bingo_sim(1000, random)