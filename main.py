import support

class player(object):
    def __init__(self, name):
        self.name = name
        self.score = 0

    def __getScore__(self):
        return self.score
    
    def add_score(self):
        self.score += 1

def start(player1, player2):

    players = {
            "X": player(player1),
            "O": player(player2)
        }
    
    game_on = True
    round_number = 1
    
    # Start the game, runs while the user doesn't quit
    while game_on:

        support.start_screen(round_number, players["X"].name, players["X"].score, players["O"].name, players["O"].score)

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

        round = True
        char = support.who_starts(players)

        # Starts a round, runs while there is no winning 
        while round:

            # Get a valid position
            position = support.get_position(players, positionDict, char)
            
            # Update board
            positionDict[position] = char

            # Check if it was a tie
            if support.check_tie(positionDict):
                support.declare_tie(positionDict)
                round = False
                game_on = support.keep_playing()

            # Check if there is a winner
            if support.check_winner(positionDict):
                support.declare_winner(positionDict, players[char].name)
                
                # Add a score point to the winner
                players[char].add_score()

                round = False
                game_on = support.keep_playing()

            # Change to next player
            char = support.change_player(char)

        # End of the round code

        round_number += 1
        
    # End of the game code

    support.show_final_winner(players)




start("one", "two")


        

