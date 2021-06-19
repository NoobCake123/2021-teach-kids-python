def print_tac_toe(a1, a2, a3, b1, b2, b3, c1, c2, c3):
    print('                1   2   3')
    print('              +-----------+')
    print('            A |', a1, '|', a2, '|', a3, '|')
    print('            B |', b1, '|', b2, '|', b3, '|')
    print('            C |', c1, '|', c2, '|', c3, '|')
    print('              +-----------+')
game_is_going = 1


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
    if turns%2 == 0:
        turns = turns+1
        move = input("player 1 what is your move?")
        if move == 'a1':
            if a1valid == 0:
                a1 = 'X'
                a1valid = a1valid+1
            else:
                print('this square is taken, please make a different move')
                turns = 0

        elif move == 'a2':
            a2 = 'X'
        elif move == 'a3':
            a3 = 'X'
        elif move == 'b1':
            b1 = 'X'
        elif move == 'b2':
            b2 = 'X'
        elif move == 'b3':
            b3 = 'X'
        elif move == 'c1':
            c1 = 'X'
        elif move == 'c2':
            c2 = 'X'
        elif move == 'c3':
            c3 = 'X'
        elif move == 'exit':
            quit()
        else:
            print("player 1 sucks")
    print_tac_toe(a1,a2,a3,b1,b2,b3,c1,c2,c3)
    if turns%2 == 1:
        turns = turns+1
        move = input("player 2 what is your move?")
        if move == 'a1':
            a1 = 'O'
        elif move == 'a2':
            a2 = 'O'
        elif move == 'a3':
            a3 = 'O'
        elif move == 'b1':
            b1 = 'O'
        elif move == 'b2':
            b2 = 'O'
        elif move == 'b3':
            b3 = 'O'
        elif move == 'c1':
            c1 = 'O'
        elif move == 'c2':
            c2 = 'O'
        elif move == 'c3':
            c3 = 'O'
        elif move == 'exit':
            quit()
        else:
            print("player 1 sucks")
    print_tac_toe(a1,a2,a3,b1,b2,b3,c1,c2,c3)


