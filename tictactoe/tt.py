board = [['7','8','9'],['4','5','6'],['1','2','3']]
playing_board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
current_letter = ['X', 'O']
count = 0

def display(lst):
    print()
    for x in range(0, len(lst)):
        print(f' {lst[x][0]} | {lst[x][1]} | {lst[x][2]} ')
        if x <= 1:
            print('-----------')
    print()

def play_game():
    choice = ''
    while choice.lower() != 'y' and choice.lower() != 'n':
        choice = input("Would you like to play tictactoe? (y/n): ")
    if choice == 'n':
        return False
    return True

def player_choice():
    global count
    choice = ''
    while not choice.isdigit():
        choice = input("Select a number on the board: ")
        if choice not in board[0] and choice not in board[1] and choice not in board[2]:
            choice = ''
    val = int(choice)
    val -= 1
    row = 1
    if val//3 == 0:
        row = 2
    elif val//3 == 2:
        row = 0
    playing_board[row][val%3] = current_letter[count%2]
    board[row][val%3] = ''

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
        count += 1
        return True
    elif count == 9:
        print("Draw")
        return True
    else:
        count += 1
        return False


def restart():
    global board, playing_board, count
    board = [['7','8','9'],['4','5','6'],['1','2','3']]
    playing_board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
    count = 0


while play_game():
    display(board)
    while not gameover(current_letter[count%2]):
        player_choice()
        display(playing_board)
    restart()
