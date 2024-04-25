"""

    Scott Quashen
    London App Brewery
    100 Days of Python Code: Day 4
    April 24 2024

    ------
    Description:    Rock paper scizzors game
    ------
    
    ------
    Inputs:         User choice in console
    ------
    
    ------
    Outputs:        Game Response
    ------
    
    ------
    Dependencies:   Random
    ------

    ------
    Assumptions:    Developed and tested using Spyder 5.15.7, Python version 3.11.5 on macOS 14.4.1
    ------
    
"""

import random


def main():
    """
    
    Description -   Runs game
    ----------
    Input -         Console
    ----------
    Output -        Console
    -------

    """
    print_rock()
    moves = ['rock', 'paper', 'scissors']
    player_move = acceptable_input('Wanna play? Make your move. (type: rock, paper, or scissors)', moves)
    comp_move = computer_move(moves)
    if comp_move == 'rock':
        print_rock()
    elif comp_move == 'paper':
        print_paper()
    else:
        print_scissors()
        
    see_who_won(player_move, comp_move)
    
    
def see_who_won(player, computer):
    """
    
    Description -   reruns main if user chooses to do so after game
    ----------
    Parameters -    User move & computer move
    ----------
    Output -        Result in console
    -------

    """

    if player == 'rock':
        if computer == 'scissors':
            print('Congrats! You just won!')
        elif computer == 'paper':
            print('Gotchya. You just lost!')
        else:
            print('Got a tie.')
    elif player == 'scissors':
        if computer == 'paper':
            print('Congrats! You just won!')
        elif computer == 'rock':
            print('Gotchya. You just lost!')
        else:
            print('Got a tie.')
    else:
        if computer == 'rock':
            print('Congrats! You just won!')
        elif computer == 'scissors':
            print('Gotchya. You just lost!')
        else:
            print('Got a tie.')
    acceptable_input('Play again?(y)', ['y'])
    main()

    
def print_rock():
    print("    _______\n--\.    ____)\n       (_____)\n       (_____)\n       (____)      \n---.__(___)\n)")

def print_paper():
    print("    _______\n--\.    ____)\n       (_______)\n       (_______)\n       (_______)      \n---.__(______)\n)")
    
def print_scissors():
    print("    _______\n--\.          ____)\n       (_____)\n            (_____)\n       (____)      \n---.__(___)\n)")
        
    


def computer_move(moves):
    """
    
    Description -   Uses random number generator to choose a move
    ----------
    Parameters -    Pass in a list of the possible moves
    ----------
    Output -        Rock, paper, or scissors
    -------

    """
    R = random.randint(0, 2)
    c_move = moves[R] 
    
    return c_move

def acceptable_input( prompt, choices ):
    """
    
    Description -   Input func modified to only accept certain values
    ----------
    Parameters -    Pass in the acceptable choices as list, and prompt
    ----------
    Output -        User's input
    -------

    """ 
    while True:
        
            
        # make sure that the result of the input is one of the acceptable choices
        
        user_input = input( prompt  ).lower() # parse string into int
        
        if user_input in choices:
            return user_input
        
        else: 
            print('Invalid input')
    
# acceptable_input
    
# run
if __name__ == '__main__':
    main()