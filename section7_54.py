
def start():
    print('Welcome to Tic Tac Toe!')

    player1_input = get_user_input()
    player1 = ''
    player2 = ''
    if (player1_input.upper() == 'X'):
        player1 = player1_input.upper()
        player2 = 'O'
    else:
        player1 = player1_input.upper()
        player2 = 'X'
    print('Player1 will go first')

    print(player1)
    print(player2)
    get_user_confirmation()

    my_list = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    game_structure(my_list)

    get_user_value(my_list, player1, player2)


def get_user_input():
    player1_input = input('Player 1: Do you want to be X or O?\n')
    if(player1_input.upper() == 'X' or player1_input.upper() == 'O'):
        return player1_input
    else:
        get_user_input()


def get_user_confirmation():
    confirmation_result = input('Are you ready to play? Enter Yes or No\n')
    if confirmation_result.upper() == 'YES':
        return
    elif confirmation_result.upper() == 'NO':
        get_user_input()
    else:
        get_user_confirmation()


def game_structure(my_list):
    my_string1 = '     |     |     '
    my_string2 = '  {0}  |  {1}  |  {2}  '
    my_string3 = '-----------------'
    print(my_string1)
    print(my_string2.format(my_list[6], my_list[7], my_list[8]))
    print(my_string1)
    print(my_string3)
    print(my_string1)
    print(my_string2.format(my_list[3], my_list[4], my_list[5]))
    print(my_string1)
    print(my_string3)
    print(my_string1)
    print(my_string2.format(my_list[0], my_list[1], my_list[2]))
    print(my_string1)


def get_user_value(my_list, player1, player2):
    if ' ' in my_list:
        user_value = input('Choose your next position (1-9): ')

        if user_value not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            get_user_value(my_list, player1, player2)
        else:
            if (already_used(user_value, my_list)):
                print('Already used')
                get_user_value(my_list, player1, player2)
            else:
                counter = check_turn(my_list)
                if (counter % 2 != 0):
                    my_list[int(user_value) - 1] = player1
                else:
                    my_list[int(user_value) - 1] = player2

                print(my_list)
                game_structure(my_list)
                if not check_winner(my_list, player1, player2, counter):
                    get_user_value(my_list, player1, player2)
    else:
        print('Game over! Nobody won')


def already_used(user_value, my_list):
    if my_list[int(user_value) - 1] != ' ':
        return True
    else:
        return False


def check_turn(my_list):
    counter = 0
    for x in my_list:
        if x == ' ':
            counter += 1

    print(counter)
    return counter


def check_winner(my_list, player1, player2, counter):
    current_player = ''
    if (counter % 2 != 0):
        current_player = player1
    else:
        current_player = player2

    if (
        (len(set(my_list[0:3])) == 1 and list(
            set(my_list[0:3]))[0] == current_player)
        or (len(set(my_list[3:6])) == 1 and list(set(my_list[3:6]))[0] == current_player)
        or (len(set(my_list[6:9])) == 1 and list(set(my_list[6:9]))[0] == current_player)
        or (len(set(my_list[0:7:3])) == 1 and list(set(my_list[0:7:3]))[0] == current_player)
        or (len(set(my_list[1:8:3])) == 1 and list(set(my_list[1:8:3]))[0] == current_player)
        or (len(set(my_list[2:9:3])) == 1 and list(set(my_list[2:9:3]))[0] == current_player)
        or (len(set(my_list[2:7:1])) == 1 and list(set(my_list[2:7:1]))[0] == current_player)
        or (len(set(my_list[0:9:3])) == 1 and list(set(my_list[0:9:3]))[0] == current_player)
    ):
        print('Winner is {}'.format(current_player))
        play_again()
        return True
    else:
        return False


def play_again():
    out = input('Do you want to play again? Enter Yes or No: ')
    if out.upper() == 'YES':
        start()
    else:
        print('Thanks for playing...GoodBye!!')


start()
