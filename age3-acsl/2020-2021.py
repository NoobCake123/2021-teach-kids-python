def trianglelist(sdr):
    for i in range(len(sdr)):
        sdr[i] = int(sdr[i])
    start = sdr[0]
    delta = sdr[1]
    rows = sdr[2]
    newstart = 0
    trianglelist = []
    for i in range(int(rows*(rows+1)/2)):
        if len(str(start)) >= 2:
            start = str(start)
            for x in start:
                newstart = newstart + int(x)
            start = newstart
            newstart = 0

        trianglelist.append(start)
        start = start + delta
    return [trianglelist,rows]
def lastrow(trianglelistrows):
    trianglelist = trianglelistrows[0]
    rows = trianglelistrows[1]
    stringofnums = ''
    for i in trianglelist:
        stringofnums += str(i)
    stringofnums = stringofnums[-rows:]
    return stringofnums
def sumoflastrow(lastrow):
    sum = 0
    for i in lastrow:
        sum += int(i)
    return sum

if __name__ == '__main__':
    for i in range(5):
        print(f'{i}.{sumoflastrow(lastrow(trianglelist(input().split(" "))))}')