board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
playing_board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
current_letter = []
count = 0


def display(lst):
    print(f'\n {lst[2][0]} | {lst[2][1]} | {lst[2][2]} ')
    print('-----------')
    print(f' {lst[1][0]} | {lst[1][1]} | {lst[1][2]} ')
    print('-----------')
    print(f' {lst[0][0]} | {lst[0][1]} | {lst[0][2]} \n')


def select_letter():
    global current_letter
    while True:
        choice = input("\nPlayer 1, select your letter (X/O): ")
        if choice.lower() == 'x':
            current_letter = ['X', 'O']
            break
        elif choice.lower() == 'o':
            current_letter = ['O', 'X']
            break
        else:
            print("Invalid response\n")


def player_choice():
    while True:
        choice = input("\nSelect a number on the board: ")
        if not any(
                choice in x for x in board) or choice == '':  # and choice not in board[1] and choice not in board[2]:
            print("Invalid response\n")
        else:
            break
    val = int(choice) - 1
    playing_board[val//3][val % 3] = current_letter[count % 2]
    board[val//3][val % 3] = ''


def gameover(letter):
    global count
    if (letter == playing_board[0][0] == playing_board[0][1] == playing_board[0][2]
            or letter == playing_board[1][0] == playing_board[1][1] == playing_board[1][2]
            or letter == playing_board[2][0] == playing_board[2][1] == playing_board[2][2]
            or letter == playing_board[0][0] == playing_board[1][0] == playing_board[2][0]
            or letter == playing_board[0][1] == playing_board[1][1] == playing_board[2][1]
            or letter == playing_board[0][2] == playing_board[1][2] == playing_board[2][2]
            or letter == playing_board[0][0] == playing_board[1][1] == playing_board[2][2]
            or letter == playing_board[0][2] == playing_board[1][1] == playing_board[2][0]):
        print(f'Winner: {letter}')
        return True
    elif count == 9:
        print("Draw")
        return True
    return False


def restart():
    global board, playing_board, count
    board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
    playing_board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    count = 0


while True:
    choice = input("Would you like to play tictactoe? (y/n): ")
    if choice.lower() == 'n':
        break
    elif choice.lower() == 'y':
        pass
    else:
        print("Invalid response\n")
        continue
    select_letter()
    display(board)
    while not gameover(current_letter[count % 2 - 1]):
        player_choice()
        count += 1
        display(playing_board)
    restart()
