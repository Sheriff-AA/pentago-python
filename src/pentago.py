import sys
from constant.ui import PRINT_BOARD_PLACE_MARBLE, PRINT_BOARD_ROTATE, PRINT_BOARD_FINISHED
from game import Game, player_finished_his_turn

from board import add_marble_to_board, is_board_full, get_position_if_valid, rotate_quarter_of_board

from render import print_game

from win import get_all_marbles_combinations_correctly_aligned

def init_game():
    try:
        name_player_1 = ask_player_name("Player 1")
        name_player_2 = ask_player_name("Player 2")
        game = Game(name_player_1, name_player_2)

        correct_combinations = []

        while is_board_full(game.board) == False and len(correct_combinations) == 0:
            print_game(game, PRINT_BOARD_PLACE_MARBLE)
            game.board = ask_player_to_place_marble(
                game.board, game.current_player_id
            )
            print_game(game, PRINT_BOARD_ROTATE)
            game.board = ask_player_to_rotate_quarter(game.board)

            game.current_player_id = player_finished_his_turn(
                game.current_player_id
            )

            correct_combinations = get_all_marbles_combinations_correctly_aligned(game.board)


        print_game(game, PRINT_BOARD_FINISHED, True, correct_combinations)

    except KeyboardInterrupt:
        sys.exit(0)
    finally:
        print("\nIt was fun, see you soon !")

def ask_player_name(default_name):
    name = input(" " + default_name +", enter your name (" +default_name+ ") :")
    if len(name) == 0:
        return default_name

    return name

def ask_player_to_place_marble(board, current_player_id):
    player_input_value_is_wrong = True;

    while player_input_value_is_wrong:
        player_input_value = input(" Place a marble: ")

        try:
            board = add_marble_to_board(board, current_player_id, player_input_value)
            player_input_value_is_wrong = False
        except ValueError:
            print(" Please play on a valid & empty cell")
            player_input_value_is_wrong = True;

    return board

def ask_player_to_rotate_quarter(board):
    player_input_value_is_wrong = True;
    
    while player_input_value_is_wrong:
        player_input_value = input(" Now rotate one quarter: ")

        try:
            board = rotate_quarter_of_board(board, player_input_value)
            player_input_value_is_wrong = False
        except ValueError:
            print("Please enter a valid rotation (1..8): ")
            player_input_value_is_wrong = True

    return board

if __name__ == "__main__":
    init_game()
