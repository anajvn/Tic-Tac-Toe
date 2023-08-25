import cutie
import os
from main import start

def show():    
    os.system('cls')

    game_type = cutie.prompt_yes_or_no(
        "Who's playing?",
        yes_text="Player vs Player",
        no_text="Player vs Computer",
        has_to_match_case=True, # The user has to type the exact case
        enter_empty_confirms=False, # An answer has to be selected
        char_prompt = False, # Exclude the [Y/N] option
        )
    
    if game_type == "Player vs Player":
        start("Player 1", "Player 2")

    elif game_type == "Player vs Computer":
        # escrever código para jogar com o pc
    
            
    
    
