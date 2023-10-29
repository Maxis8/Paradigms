# Написать игру в “Крестики-нолики”. Можете использовать
# любые парадигмы, которые посчитаете наиболее
# подходящими. Можете реализовать доску как угодно - как
# одномерный массив или двумерный массив (массив массивов).
# Можете использовать как правила, так и хардкод, на своё
# усмотрение. Главное, чтобы в игру можно было поиграть через
# терминал с вашего компьютера.

print('Start!')

board_list = list(range(1,10))

def desk(board):
    print('-'*12)
    for i in range(3):
        print('|', board[0+i*3],'|', board[1+i*3], '|', board[2+i*3], '|')
        print('-'*12)

def choice(tic_tac):
    valid = False
    while not valid:
        player_index = input('Your move ' + tic_tac + ' --> ')
        try:
            player_index =int(player_index)
        except:
            print('Enter number!')
            continue
        if 1 <= player_index <= 9:
            if str(board_list[player_index - 1]) not in 'X0':
                board_list[player_index-1] = tic_tac
                valid = True
            else:
                print('Busy!')
        else:
            print('Try again 1-9! ')

def check_win(board):
    win = ((0,1,2),(3,4,5),(6,7,8),
               (0,3,6),(1,4,7),(2,5,8),
               (0,4,8),(2,4,6))
    for i in win:
        if board[i[0]] == board[i[1]] == board[i[2]]:
            return board[i[0]]
    return False

def game(board):
    count =0
    victory = False
    while not victory:
        desk(board)
        if count % 2 == 0:
            choice('X')
        else:
            choice('0')
        count +=1
        print(count)
        if count > 4:
            win_tab = check_win(board)
            if win_tab:
                print(win_tab,'Win!')
                victory = True

            elif count == 9:
                print('Game draw!')
                victory =True
        desk(board)
game(board_list)

