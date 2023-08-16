import os
import time

positiondict = {
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9
}

board = """ TIC TAC TOE
| %s | %s | %s |
| %s | %s | %s |
| %s | %s | %s |""" % (positiondict["1"], positiondict["2"], positiondict["3"], positiondict["4"], positiondict["5"], positiondict["6"], positiondict["7"], positiondict["8"], positiondict["9"])

game_on = True
char = "X"

# Starts the game, runs while there is no winning 
while game_on:
    
    answer_not_compatible = True
    position = ""

    while answer_not_compatible:
        # Clear screen to start only with the board updated and asking the new input
        os.system('cls')

        # Print board and ask input
        print(board + "\n")
        position = input("Enter position of %s: " % char)

        # Checks if the answer is a valid position
        try:
            positiondict[position]
            
            if positiondict[position] == "X" or positiondict[position]== "O":
                raise Exception("Position already chosen.")

            answer_not_compatible = False

        except:
            print("Position not valid, choose an available number")
            time.sleep(2)
        
    
    # Update board
    positiondict[position] = char
    print(positiondict.values())
    time.sleep(5)
    # Change to next player
    if char == "X":
        char = "O"
    else:
        char ="X"
    

