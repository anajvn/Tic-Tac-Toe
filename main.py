import time
import support

positionDict = {
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

players = {
    "X": "Player 1",
    "O": "Player 2"
}

game_on = True
char = "X"

# Starts the game, runs while there is no winning 
while game_on:
    
    answer_not_compatible = True
    position = ""

    while answer_not_compatible:
        # Clear screen to start only with the board updated and asking the new input
        support.clear()

        # Print board and ask input
        support.draw_board(positionDict)
        position = input("%s turn - Enter position of %s: " % (players[char], char))

        # Checks if the answer is a valid position
        try:
            positionDict[position]
            
            if positionDict[position] == "X" or positionDict[position]== "O":
                raise Exception("Position already chosen.")

            answer_not_compatible = False

        except:
            print("Position not valid, choose an available number")
            time.sleep(2)
        
    
    # Update board
    positionDict[position] = char

    # Check if it was a tie
    if support.check_tie(positionDict):
        support.declare_tie(positionDict)
        game_on = False

    # Check if there is a winner
    if support.check_winner(positionDict):
        support.declare_winner(positionDict, players[char])
        game_on = False

    # Change to next player
    char = support.change_player(char)
    

