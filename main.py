import use_cases

def start(player1, player2):

    players = use_cases.create_players(player1, player2)
    
    game_on = True
    round_number = 1
    
    # Start the game, runs while the user doesn't quit
    while game_on:

        use_cases.start_round(round_number, players)
        board = use_cases.create_board()
        round = True
        char = use_cases.initiator(players)
            
        # Starts a round, runs while there is no winning 
        while round:

            if  (player2 == "Computer" and char == "X") or (player2 == "Player 2"):
                # Get user input and update the board
                use_cases.user_input(board, players, char)

                # Check for a tie or victory and returns if the round is over
                round = use_cases.victory_or_tie(board, players, char)
                if not round:
                    game_on = use_cases.keep_playing()
                    continue
                char = use_cases.change_player(char)

            # Call computer turn
            if player2 == "Computer":
                use_cases.play_round_auto(board, char)
                # Check for a tie or victory and returns if the round is over
                round = use_cases.victory_or_tie(board, players, char)
                if not round:
                    game_on = use_cases.keep_playing()
                char = use_cases.change_player(char)
                
        # End of the round code
        round_number += 1
        
    # End of the game code

    use_cases.show_final_winner(players)