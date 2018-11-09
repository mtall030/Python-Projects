import itertools

def game_board(game_map, player=0, row=0, column=0, just_display=False):
    try:
        if game_map[row][column] != 0:
            print('This position is occupied. Chose another.')
            return game_map, False
        #print ('   a  b  c')
        print ("   "+"   ".join([str(i) for i in range(len(game_map))]))
        if not just_display:
            game_map[row][column] = player
        for count, row in enumerate(game_map):
            print(count, row)
        return game_map, True
        
    except IndexError as e:
        print ("Error: make you input row/column as 0, 1, or 2?", e)
        return game_map, False
    except Exception as e:
        print ("Something went very wrong!", e)
        return game_map, False

def win(current_game):

    #checking list for a win
    def all_same(l):
        if l.count(l[0]) == len(l) and l[0] != 0:
            return True
        else:
            return False

    #horizontal winner
    for row in game:
        print (row)
        if all_same(row):
            print (f'Player {row[0]} is the winner horizonally (-)!')
            return True
            
    #verital winner
    for col in range(len(game)):
        check = []
        for row in game:
            check.append(row[col])
        if all_same(check):
                print (f'Player {row[0]} is the winner vertically (|)!')
                return True
    
    #diagonal winner
    diags = []
    for ix in range(len(game)):
        diags.append(game[ix][ix])
    if all_same(diags):
        print (f'Player {diags[0]} is the winner diagonally (\\)!')
        return True

    diags = []
    for col, row in enumerate(reversed(range(len(game)))):
        diags.append(game[row][col])
    if all_same(diags):
        print (f'Player {diags[0]} is the winner diagonally (/)!')
        return True

    return False

play = True
players = [1,2]
while play:
    game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]

    game_won = False
    game, _ = game_board(game, just_display = True)
    player_choice = itertools.cycle([1, 2])
    while not game_won:
        current_player = next(player_choice)
        print (f'Current PLayer: {current_player}')

        played = False
        while not played:
            column_choice = int(input('What column do you want to play? (0, 1, 2): '))
            row_choice = int(input('What row do you want to play? (0, 1, 2): '))
            game, played = game_board(game, player = current_player, row = row_choice, column = column_choice)

        if win(game):
            game_won = True
            again = input('Game Over, would you like to play again?: ')
            if again.lower() == 'y':
                print ('Restarting...')
            elif again.lower() == 'n':
                print ('Bye !')
                play = False
            else:
                print ('Not a valid answer, peace out!')
                play = False
