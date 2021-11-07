import random
def swap_case(s):
    s = list(s)
    newa = []
    finala = ''
    for i in range(len(s)):
        if i%2 == 1:
            if ord(s[i]) > 64 and ord(s[i]) < 91:
                newa.append(chr(ord(s[i])+32))
            elif ord(s[i]) > 96 and ord(s[i]) < 123:
                newa.append(chr(ord(s[i])-32))
            else:
                newa.append(s[i])
        else:
            newa.append(s[i])
    for i in newa:
        finala += i
    return finala
if __name__ == '__main__':
    insults = ["your trash",'bruh really?', "nIcE","i'm not impressed.","DUDE IMAGINE LOLOLOL","cringe"]
    print("Hello. I am nice Chatbot.")
    while 1 < 2:
        expression = input()
        print(swap_case(expression))
        print(insults[random.randint(0,5)])

