def print_tac_toe(a1, a2, a3, b1, b2, b3, c1, c2, c3):
    print('                1   2   3')
    print('              +-----------+')
    print('            A |', a1, '|', a2, '|', a3, '|')
    print('            B |', b1, '|', b2, '|', b3, '|')
    print('            C |', c1, '|', c2, '|', c3, '|')
    print('              +-----------+')


print('''
********************************************
              TIC TAC TOE MENU    
********************************************
COMMANDS: Type in "exit" without quotation
marks to exit the game. To place a circle or
cross on the board, first type the row letter
then the column letter, e.g. A1, C3, etc...''')
a1 = a2 = a3 = b1 = b2 = b3 = c1 = c2 = c3 = ' '
turns = 0
game_is_going = 1
a1valid = 0
a2valid = 0
a3valid = 0
b1valid = 0
b2valid = 0
b3valid = 0
c1valid = 0
c2valid = 0
c3valid = 0



printictac = print_tac_toe(a1, a2, a3, b1, b2, b3, c1, c2, c3)
while game_is_going == 1:
    if turns % 2 == 0:
        game_is_going = 0
        turns = turns + 1
        move = input("player 1 what is your move?")
        if move == 'a1':
            if a1valid == 0:
                a1 = 'X'
                a1valid = a1valid + 1
            else:
                print('this square is taken, please make a different move')
                turns = 0

        elif move == 'a2':
            if a2valid == 0:
                a2 = 'X'
                a2valid = a2valid + 1
            else:
                print('this square is taken, please make a different move')
                turns = 0
        elif move == 'a3':
            if a3valid == 0:
                a3 = 'X'
                a3valid = a3valid + 1
            else:
                print('this square is taken, please make a different move')
                turns = 0
        elif move == 'b1':
            if b1valid == 0:
                b1 = 'X'
                b1valid = b1valid + 1
            else:
                print('this square is taken, please make a different move')
                turns = 0
        elif move == 'b2':
            if b2valid == 0:
                b2 = 'X'
                b2valid = b2valid + 1
            else:
                print('this square is taken, please make a different move')
                turns = 0
        elif move == 'b3':
            if b3valid == 0:
                b3 = 'X'
                b3alid = b3valid + 1
            else:
                print('this square is taken, please make a different move')
                turns = 0
        elif move == 'c1':
            if c1valid == 0:
                c1 = 'X'
                c1valid = c1valid + 1
            else:
                print('this square is taken, please make a different move')
                turns = 0
        elif move == 'c2':
            if c2valid == 0:
                c2 = 'X'
                c2valid = c2valid + 1
            else:
                print('this square is taken, please make a different move')
                turns = 0
        elif move == 'c3':
            if c3valid == 0:
                c3 = 'X'
                c3valid = c3valid + 1
            else:
                print('this square is taken, please make a different move')
                turns = 0
        elif move == 'exit':
            quit()
        else:
            print("player 1 sucks")
    print_tac_toe(a1, a2, a3, b1, b2, b3, c1, c2, c3)
    if turns % 2 == 1:
        turns = turns + 1
        move = input("player 2 what is your move?")
        if move == 'a1':
            if a1valid == 0:
                a1 = 'O'
                a1valid = a1valid + 1
            else:
                print('this square is taken, please make a different move')
                turns = 1
        elif move == 'a2':
            if a2valid == 0:
                a2 = 'O'
                a2valid = a2valid + 1
            else:
                print('this square is taken, please make a different move')
                turns = 1
        elif move == 'a3':
            if a3valid == 0:
                a3 = 'O'
                a3valid = a3valid + 1
            else:
                print('this square is taken, please make a different move')
                turns = 1
        elif move == 'b1':
            if b1valid == 0:
                b1 = 'O'
                b1valid = b1valid + 1
            else:
                print('this square is taken, please make a different move')
                turns = 1
        elif move == 'b2':
            if b2valid == 0:
                b2 = 'O'
                b2valid = b2valid + 1
            else:
                print('tis square is taken, please make a different move')
                turns = 1
        elif move == 'b3':
            if b3valid == 0:
                b3 = 'O'
                b3valid = b3valid + 1
            else:
                print('this square is taken, please make a different move')
                turns = 1
        elif move == 'c1':
            if c1valid == 0:
                c1 = 'O'
                c1valid = c1valid + 1
            else:
                print('this square is taken, please make a different move')
                turns = 1
        elif move == 'c2':
            if c2valid == 0:
                c2 = 'O'
                c2valid = c2valid + 1
            else:
                print('this square is taken, please make a different move')
                turns = 1
        elif move == 'c3':
            if c3valid == 0:
                c3 = 'O'
                c3valid = c3valid + 1
            else:
                print('this square is taken, please make a different move')
                turns = 1
        elif move == 'exit':
            quit()
        else:
            print("player 2 sucks")
    print_tac_toe(a1, a2, a3, b1, b2, b3, c1, c2, c3)
if game_is_going == 0:
    print("It's a tie...")
    quit()
