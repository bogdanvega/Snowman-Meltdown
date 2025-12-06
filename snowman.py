from game_logic import play_game

if __name__ == "__main__":
    """ Main function that calls the game function and allows the user to play again. """
    while True:
        play_game()
        replay = input("Do you want to play another game? (yes/no) ")
        if replay == "yes":
            continue
        break