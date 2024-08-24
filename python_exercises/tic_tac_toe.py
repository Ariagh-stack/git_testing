from colorama import Fore, Style

player, computer = 'X', 'O'
print("Player: X\nComputer: O")
board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
win_sit = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
move_priority = ((1, 7, 3, 9), (5,), (2, 4, 6, 8))


def print_board():
    j = 1
    for i in board:
        end = "\t"
        if j % 3 == 0:
            end = "\n\n"
        if i == "X":
            print(f"{Fore.RED}[{i}]{Style.RESET_ALL}", end=end)
        elif i == "O":
            print(f"{Fore.BLUE}[{i}]{Style.RESET_ALL}", end=end)
        else:
            print(f"[{i}]", end=end)
        j += 1


def make_move(brd, plyr, mve, undo=False):
    if can_move(brd, mve):
        brd[mve-1] = plyr
        win = is_winner(brd, plyr)
        if undo:
            brd[mve-1] = mve
        return True, win
    return False, False


def can_move(brd, mve):
    if mve in range(1, 10) and isinstance(brd[mve-1], int):
        return True
    return False


def is_winner(brd, plyr):
    win = True
    for tuple in win_sit:
        win = True
        for j in tuple:
            if brd[j] != plyr:
                win = False
                break
        if win:
            break
    return win


def has_empty_space():
    return board.count("X") + board.count("O") != 9


def the_AI_move():
    mv = -1
    # if the AI itself could win the game?
    for i in range(1, 10):
        if make_move(board, computer, i, True)[1]:
            mv = i
            break
    # if the player is winning, the AI should stop it.
    if mv == -1:
        for j in range(1, 10):
            if make_move(board, computer, i, True)[1]:
                mv = j
                break
    # AI moves now.
    if mv == -1:
        for tup in move_priority:
            for m in tup:
                if mv == -1 and can_move(board, m):
                    mv = m
                    break
    return make_move(board, computer, mv)


while has_empty_space():
    print_board()
    move = int(input("choose your move(1-9):"))
    moved, won = make_move(board, player, move)
    if not moved:
        print("invalid move! Try again!")
        continue
    if won:
        print(f"{Fore.GREEN}Congratulations! Player Won!{Style.RESET_ALL}")
        break
    elif the_AI_move()[1]:
        print(f"{Fore.YELLOW}You lost!{Style.RESET_ALL}")


