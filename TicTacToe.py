while True:
    print("Let's play Tic Tac Toe!")

    # Initialize boolean that will determine when the game is over.
    game_over = False

    # Define empty dictionaries that will contain player data.
    p1 = {}
    p2 = {}

    # Ask players for names and enter into dictionary.
    p1['name'] = input('Player 1, please enter your name: ')
    p2['name'] = input('Player 2, please enter your name: ')
    players = [p1, p2]
                       
    # Randomly determine which player goes first and ask which marker they want.
    from random import randint
    starter = randint(0, 1)
    second = abs(1-starter)

    print('It has randomly been determined that ' + players[starter]['name'] + ' will start.')

    # Ask starting player which marker they want until a valid marker is entered.
    markers = ['X', 'O']

    players[starter]['marker'] = ''
    while players[starter]['marker'] not in markers:
        players[starter]['marker'] = input(players[starter]['name'] + ', do you you want to be X or O? ').upper()
        if players[starter]['marker'] not in markers:
            print('That is not a valid marker.  Please try again.')
            continue

    # Assign remaining marker to the other player.
    markers.remove(players[starter]['marker'])
    players[second]['marker'] = markers[0]

    # Create list that will contain game data.  The 0th element will remain blank to avoid index confusion.
    gameboard = [' ']*10

    # Create sets that will contain all remaining and used positions on the board.
    remaining = set(range(1, 10))
    used = set({})

    # Define function that will display current status of the board.
    def display_board(board):
        print('   |   |')
        print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
        print('   |   |')

    # Define a function to get input from user that checks that input is valid.
    def get_input(name):
        move = ''
        while move not in remaining:
            move = input(name + ', please choose a position (1-9): ')
            if move not in {str(x) for x in set(range(0, 10))}:
                print('That is not a valid position.  Please try again.')
                continue
            elif move in {str(x) for x in used}:
                print('That position is already taken.  Please try again.')
                continue
            else:
                return int(move)

     # Define a function to see if a player has won.
    def is_winner(marker):
        if gameboard[1] == marker and gameboard[2] == marker and gameboard[3] == marker:
            return True
        elif gameboard[4] == marker and gameboard[5] == marker and gameboard[6] == marker:
            return True
        elif gameboard[7] == marker and gameboard[8] == marker and gameboard[9] == marker:
            return True
        elif gameboard[1] == marker and gameboard[4] == marker and gameboard[7] == marker:
            return True
        elif gameboard[2] == marker and gameboard[5] == marker and gameboard[8] == marker:
            return True
        elif gameboard[3] == marker and gameboard[6] == marker and gameboard[9] == marker:
            return True
        elif gameboard[1] == marker and gameboard[5] == marker and gameboard[9] == marker:
            return True
        elif gameboard[7] == marker and gameboard[5] == marker and gameboard[3] == marker:
            return True
        else:
            return False

    # Define a function to check if the board is full.
    def board_full():
        if len(used) == 9:
            return True
        
    # Define a function that asks a player for their move, updates remaining and used lists, updates the game board
    # and displays the results and then checks to see if the game should be over.
    def game_play(player):
        global game_over
        current_move = get_input(players[player]['name'])
        remaining.discard(current_move)
        used.add(current_move)
        gameboard[current_move] = players[player]['marker']
        display_board(gameboard)
        if is_winner(players[player]['marker']):
            print(players[player]['name'], 'is the winner!')
            game_over = True
        elif board_full():
            print('There are no more possible moves.  The game is a draw!')
            game_over = True

    # Define a function to ask if they want to play again.
    def play_again():
        return input("Type 'y' to play again or any other key to exit ").lower().startswith('y')

    # Time to play the game.

    # Display initial blank game board.
    display_board(gameboard)

    # Alternate turns until either someone has won or the board is full.
    while not game_over:
        game_play(starter)
        if game_over:           
            break
        
        game_play(second)
        if game_over:
            break
        
    # Ask if they want to play again.        
    if play_again():
        continue
    else:
        print('See you next time!')
        break           
