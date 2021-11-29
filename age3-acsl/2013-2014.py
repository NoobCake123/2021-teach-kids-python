
def parsedata(word,place):
    #i need the letters, n their placements?
    letterscores = []
    places = []
    for spot in range(len(word)):
        places.append(place+spot)
    for letter in word:
        if letter in ['A','E']:
            letterscores.append(1)
        elif letter in ['D','R']:
            letterscores.append(2)
        elif letter in ['B','M']:
            letterscores.append(3)
        elif letter in ['V','Y']:
            letterscores.append(4)
        elif letter in ['J','X']:
            letterscores.append(8)
    #places = [1,2,3,4] letterscores = [8,1,4,1]
    return [letterscores,places]
def mults(letterscoresnplaces):
    letterscores = letterscoresnplaces[0]
    isdouble = False
    istriple = False
    places = letterscoresnplaces[1]
    for i in range(len(places)):
        if places[i] % 6 == 3:
            letterscores[i] = letterscores[i]*2
        elif places[i] % 5 == 0:
            letterscores[i] = letterscores[i]*3
        elif places[i] % 7 == 0 and places[i] % 8 != 0:
            isdouble = True
        elif places[i] % 8 == 0:
            istriple = True
    return [letterscores,isdouble,istriple]
def finalscore(boolnscores):
    letterscores = boolnscores[0]
    isdouble = boolnscores[1]
    istriple = boolnscores[2]
    grosstotal = 0
    for i in letterscores:
        grosstotal = grosstotal + i
    if isdouble == True and istriple == False:
        grosstotal = grosstotal*2
    elif istriple == True:
        grosstotal = grosstotal*3
    return grosstotal
if __name__ == '__main__':
    listofinputs = []
    line1 = input('1. ').split(', ')
    for i in range(5):
        listofinputs.append(int(input(f'{i+2}.')))
    for i in range(5):
        print(f'{i+1}. {finalscore(mults(parsedata(line1,listofinputs[i])))}')
