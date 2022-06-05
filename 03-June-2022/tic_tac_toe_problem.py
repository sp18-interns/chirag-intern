import random
# from IPython.display import clear_output

def display_board(board):
    print('   |   |')
    print('  '+board[7] + '| ' + board[8]+' '+'|'+'  '+board[9])
    print('   |   |')
    print('-------------')
    print('   |   |')
    print('  '+board[4] + '| ' + board[5]+' '+'|'+'  '+board[6])
    print('   |   |')
    print('-------------')
    print('   |   |')
    print('  '+board[1] + '| ' + board[2]+' '+'|'+'  '+board[3])
    print('   |   |')

test_board = ['X','X','O','X','O','X','O','X','O','X']
display_board(test_board)

def player_input():
    marker = ''

    while marker != 'X' and marker != 'O':
        marker = input('Player 1, choose X or O :').upper()


    if marker == 'X':
        return('X','O')
    else:
        return('O','X')

player_input()


def place_marker(board ,marker, position):
    board[position] = marker
    place_marker(test_board,'#',8)
    display_board(test_board)

def win_check(board,mark):
    display_board(board)
    if mark == 'X':
        mark1 = 'O'

    if board[1] == board[2] and board[2] == board[3]:
        if mark == board[1]:
            print(f'Mark {mark} won!')
        else:
            print(f'Mark {mark1} won!')
    elif board[1] == board[4] and board[4] == board[7]:
        if mark == board[1]:
            print(f'Mark {mark} won!')
        else:
            print(f'Mark {mark1} won!')
    elif board[1] == board[5] and board[5] == board[9]:
        if mark == board[1]:
            print(f'Mark {mark} won!')
        else:
            print(f'Mark {mark1} won!')
    elif board[2] == board[5] and board[5] == board[8]:
        if mark == board[2]:
            print(f'Mark {mark} won!')
        else:
            print(f'Mark {mark1} won!')
    elif board[3] == board[6] and board[6] == board[9]:
        if mark == board[3]:
            print(f'Mark {mark} won!')
        else:
            print(f'Mark {mark1} won!')
    elif board[3] == board[5] and board[5] == board[7]:
        if mark == board[3]:
            print(f'Mark {mark} won!')
        else:
            print(f'Mark {mark1} won!')
    elif board[4] == board[5] and board[5] == board[6]:
        if mark == board[4]:
            print(f'Mark {mark} won!')
        else:
            print(f'Mark {mark1} won!')
    elif board[7] == board[8] and board[8] == board[9]:
        if mark == board[7]:
            print(f'Mark {mark} won!')
        else:
            print(f'Mark {mark1} won!')
    else:
        print('Match Drawn')

win_check(test_board,'X')

def choose_first():
    return random.randint()

def space_check(board, position):
    position=0
    for position in board:
        if board[position]== '':
            break
    return True

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
        return True


def player_choice(board):
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))

    return position





def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


print('Welcome to Tic Tac Toe!')
test_board=['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
player1, player2=player_input()
display_board(test_board)
player_choice(test_board)
space_check(test_board,position)
place_marker(test_board,marker,position)
full_board_check()
replay()
