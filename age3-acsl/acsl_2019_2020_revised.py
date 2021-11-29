def converter(line1):
    n = line1[0]
    p = int(line1[1])
    d = int(line1[2])
    if p > 1:
        n = n[:-p + 1]
    pthdigit = n[len(n) - 1]
    n = n[:-1]
    if int(pthdigit) <= 4:
        n = n + str((int(pthdigit) + d) % 10)
    elif int(pthdigit) >= 5:
        n = n + str(abs(int(pthdigit) - d))[:1]
    for i in range(p - 1):
        n = n + '0'
    return n

def exitprint(msg):
    print(f"That isn't valid! {msg}")
    exit(-1)
def isitvalid(line1):
    #isitvalid
    if len(line1) != 3:
        #if there are more spaces
        exitprint('There are too many spaces')
    elif len(line1[0]) < int(line1[1]):
        print("That isn't valid. Why so mean?")
        exit(-1)
    elif len(line1[0]) >= 15:
        print("That isn't valid. Your number was too big")
        exit(-1)
        #p has to be positive
        #p and d r integers
    else:
        return line1



if __name__ == '__main__':
    listofinputs = []
    for i in range(5):
        temp = input().split(' ')
        isitvalid(temp)
        listofinputs.append(temp)

    for i in listofinputs:
        print(converter(i))
