def permspart(binlist):
    permlist = []
    permi = ''
    for i in binlist:
        permi = ''
        for x in range(len(i)):
            x = int(x)
            a = int(i[x])
            if a == 1 and x == 0:
                permi = permi + 'r'
            elif a == 0 and x == 0:
                permi = permi + '-'
            elif a == 1 and x == 1:
                permi = permi + 'w'
            elif a == 0 and x == 1:
                permi = permi + '-'
            elif a == 1 and x == 2:
                permi = permi + 'x'
            elif a == 0 and x == 2:
                permi = permi + '-'
        permlist.append(permi)
    return permlist


def binpart(line1):
    binarynum = ''
    for i in line1:
        digitbin = bin(int(i))[2:]
        while len(digitbin) < 3:
            digitbin = '0' + digitbin
        binarynum = binarynum + digitbin
        binarynum = binarynum + ' '

    return binarynum


if __name__ == '__main__':
    for i in range(5):
        lin1 = input(f'{i+1}.')
        print(f"{i+1}.{binpart(lin1.split(', '))}and {' '.join(permspart(binpart(lin1.split(', '))[:-1].split(' ')))}")
