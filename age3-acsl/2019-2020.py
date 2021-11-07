
if __name__ == '__main__':
    n = '139857135'
    p = 3
    d = 7
    n = n[:-p+1]

    for i in range(p-1):
        n = n+'0'
    print(n)
