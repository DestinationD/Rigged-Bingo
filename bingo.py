from random import choice, getrandbits, randint

roll_record = []

def draw(biased):
    # assumption: biased is boolean or 0 & 1
    if biased:
        return # return random_draw()
    elif not biased:
        return randint(1,36)
    else:
        print("You messed up somewhere!")


def check_win(board):
    # We know our win conditions, so check
    # the board
    lines = 0
    # Check horizontal and vertical lines
    for i in range(6):
            
        if(all(x in roll_record for x in board[:][i])):
            lines += 1
        
        if(all(x in roll_record for x in board[i][:])):
            lines += 1
    
    # Check diagonals
    diag = [board[i][i] for i in range(6)]
    ndiag = [board[i][~i] for i in range(6)]
    
    if(all(x in roll_record for x in diag)):
        lines += 1
    if(all(x in roll_record for x in ndiag)):
        lines += 1
    
    if (lines == 0):
        print("No lines have been formed.")
    elif (lines < 14):
        print(f'{lines} lines have been formed!')
    else:
        print("The board has been cleared!")
        
def roll(runs):
    """
    Creates a list equal to length of the parameter, filled with randomly drawn numbers.
    """
    roll_length = runs
    for x in range(roll_length):
        roll_record.append(draw(0))
    print(roll_record)
    

roll(36)