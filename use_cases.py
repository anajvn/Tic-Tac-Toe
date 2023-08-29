import support
import entities

def create_players(name_1, name_2):
    return {"X": entities.player(name_1),
            "O": entities.player(name_2)}
    
def create_board():
    return entities.board()

# Show the start screen and the game score
def start_round(round, players):
    support.clear()
    print("""
      -----------\n
      | ROUND %s |\n
      -----------\n
%s - %s vs %s - %s\n""" 
          % (round, players["X"].name, players["X"].score, players["O"].name, players["O"].score))
    support.wait(3)

# Defines the player that will starts
def initiator(players):
    support.clear()
    player = support.random_player()
    print("%s will start this round..." % players[player].name)
    support.wait(3)

    return player

# Get the user position and update the board
def user_input(board, players, char):

    # Get a valid position
    position = support.get_position(players, board, char)
    
    # Update board
    board.change_position(position, char)

# Verifies if there is a tie or a victory
def victory_or_tie(board, players, char):

    if support.check_tie(board):
        support.declare_tie(board)
        return False

    # Check if there is a winner
    if support.check_winner(board):
        support.declare_winner(board, players[char].name)
        
        # Add a score point to the winner
        players[char].add_score()

        return False
    
    return True

# Continue playing the game
def keep_playing():
    answer = input("Would you like to keep playing (Y/N)? ").lower()

    if answer == "y" or answer == "yes":
        return True
    
    return False

# Change player from X to O or the opposite
def change_player(char):
    if char == "X":
        char = "O"
    else:
        char ="X"
    
    return char

# Show the winner based on the score
def show_final_winner(players):
    support.clear()
    if players["X"].score > players["O"].score:
        print("%s is the winner!" % players["X"].name)
    else:
        print("%s is the winner!" % players["O"].name)
