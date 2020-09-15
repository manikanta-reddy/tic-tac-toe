
def draw_board(char_list):
    """installing the board"""
    print("\n\t   Tic-Tac-Toe")
    print("\t-----------------")
    print(f"\t|| {char_list[0]} || {char_list[1]} || {char_list[2]} ||")
    print("\t-----------------")
    print(f"\t|| {char_list[3]} || {char_list[4]} || {char_list[5]} ||")
    print("\t-----------------")
    print(f"\t|| {char_list[6]} || {char_list[7]} || {char_list[8]} ||")
    print("\t-----------------")


def get_player_input(player_char, char_list):
    """Getting the players input"""
    while True:
        move = int(input(f"{player_char}: Where would you like to place your move (1 to 9): "))
        if 0 < move < 10:
            if char_list[move - 1] == "_":
                return move
            else:
                print("That spot has already been choosen. Try again.")
        else:
            print("That is not a spot on the board. Try again")


def place_char_on_board(player_char, move, char_list):
    """Replacing the player move in "_" """
    char_list[move - 1] = player_char


def is_winner(cl, pc):
    """Winner deciding """
    return ((cl[0] == pc and cl[1] == pc and cl[2] == pc) or  # first row
            (cl[3] == pc and cl[4] == pc and cl[5] == pc) or  # second row
            (cl[6] == pc and cl[7] == pc and cl[8] == pc) or  # third row
            (cl[0] == pc and cl[3] == pc and cl[6] == pc) or  # 1 column
            (cl[1] == pc and cl[4] == pc and cl[7] == pc) or  # 2 column
            (cl[2] == pc and cl[5] == pc and cl[8] == pc) or  # 3 column
            (cl[0] == pc and cl[4] == pc and cl[8] == pc) or  # diagonal
            (cl[2] == pc and cl[4] == pc and cl[6] == pc))


# main loop
player_1 = 'X'
player_2 = 'O'
c_list = ['_'] * 9
n_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
# draw board
draw_board(n_list)
draw_board(c_list)
while True:
    # player-1 turn
    p1move = get_player_input(player_1, c_list)
    place_char_on_board(player_1, p1move, c_list)
    draw_board(n_list)
    draw_board(c_list)

    if is_winner(c_list, player_1):
        print("Player 1 Wins!!")
        break
    elif "_" not in c_list:
        print("The game was a tie!")
        break

    # player-2 turn
    p2move = get_player_input(player_2, c_list)
    place_char_on_board(player_2, p2move, c_list)
    draw_board(n_list)
    draw_board(c_list)

    if is_winner(c_list, player_2):
        print("Player 2 Wins!!")
        break
