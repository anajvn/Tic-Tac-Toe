import os
import time
from random import randint

### GLOBAL METHODS

# Clear screen
def clear():
    os.system('cls')

### ROUND METHODS

# Draw updated board
def draw_board(positiondict):
    board = """ TIC-TAC-TOE
| %s | %s | %s |
| %s | %s | %s |
| %s | %s | %s |""" % (positiondict["1"], positiondict["2"], positiondict["3"], \
                       positiondict["4"], positiondict["5"], positiondict["6"], \
                       positiondict["7"], positiondict["8"], positiondict["9"])

    print(board + "\n")

# Get valid position
def get_position(players, positionDict, char):

    answer_not_compatible = True
    position = ""


    while answer_not_compatible:
        # Clear screen to start only with the board updated and asking the new input
        clear()

        # Print board and ask input
        draw_board(positionDict)
        position = input("%s turn - Enter position of %s: " % (players[char].name, char))

        # Checks if the answer is a valid position
        try:
            positionDict[position]
            
            if positionDict[position] == "X" or positionDict[position]== "O":
                raise Exception("Position already chosen.")

            answer_not_compatible = False

        except:
            print("Position not valid, choose an available number")
            time.sleep(2)
    
    return position

# Change player from X to O or the opposite
def change_player(char):
    if char == "X":
        char = "O"
    else:
        char ="X"
    
    return char

# Check winners
def check_winner(positiondict):
    """ Possible combinations:
    1 - 2 - 3 | 4 - 5 - 6 | 7 - 8 - 9
    1 - 4 - 7 | 2 - 5 - 8 | 3 - 6 - 9
    1 - 5 - 9 | 3 - 5 - 7
    """

    if (positiondict["1"] == positiondict["2"] == positiondict["3"]) \
    or (positiondict["4"] == positiondict["5"] == positiondict["6"]) \
    or (positiondict["7"] == positiondict["8"] == positiondict["9"]) \
    or (positiondict["1"] == positiondict["4"] == positiondict["7"]) \
    or (positiondict["2"] == positiondict["5"] == positiondict["8"]) \
    or (positiondict["3"] == positiondict["6"] == positiondict["9"]) \
    or (positiondict["1"] == positiondict["5"] == positiondict["9"]) \
    or (positiondict["3"] == positiondict["5"] == positiondict["7"]):
        return True
    else:
        return False
    
# Declare the winner with the updated board
def declare_winner(positionDict, winner):
    # Clear screen to start only with the board updated
    clear()

    # Print board with the victory
    draw_board(positionDict)
    print("Yay! %s won the game!" % winner)

# Check if the board is complete and it was a tie
def check_tie(positiondict):
    values = positiondict.values()
    count = 0 
    for value in values:
        if value == "X" or value == "O":
            count += 1
        
    return count == 9

# Declare a tie with the updated board
def declare_tie(positionDict):
    # Clear screen to start only with the board updated
    clear()

    # Print board with the tie
    draw_board(positionDict)
    print("Round has ended. It was a tie!")

# Continue playing the game
def keep_playing():
    answer = input("Would you like to keep playing (Y/N)? ")

    if answer == "Y" or answer == "y":
        return True
    
    return False

### GAME METHODS

def start_screen(round, name1, point1, name2, point2):

    clear()
    print("-----------\n| ROUND %s |\n-----------\n%s vs %s\n %s     %s " % (round, name1, name2, point1, point2))
    time.sleep(3)

# Define which char starts
def who_starts(players):
    index = randint(1, 11)
    char = ""

    if index <= 5:
        char = "X"
    else:
        char = "O"
    
    clear()
    print("%s will start this round..." % players[char].name)
    time.sleep(3)
    return char

def show_final_winner(players):
    
    clear()

    if players["X"].score > players["O"].score:
        print("%s is the winner!" % players["X"].name)
    else:
        print("%s is the winner!" % players["O"].name)




