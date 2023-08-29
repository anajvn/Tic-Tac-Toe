import support
import use_cases

def start(player1, player2):

    players = use_cases.create_players(player1, player2)
    
    game_on = True
    round_number = 1
    
    # Start the game, runs while the user doesn't quit
    while game_on:

        # use_cases.start_round(round_number, players)
        board = use_cases.create_board()


        round = True
        char = use_cases.initiator(players)

        # Starts a round, runs while there is no winning 
        while round:

            # Get user input and update the board
            use_cases.user_input(board, players, char)

            # Check for a tie or victory and returns if the round is over
            round = use_cases.victory_or_tie(board, players, char)
            if not round:
                game_on = support.keep_playing()

            # Change to next player
            char = support.change_player(char)

        # End of the round code
        round_number += 1
        
    # End of the game code

    support.show_final_winner(players)