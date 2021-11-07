
if __name__ == '__main__':
    n = '139857135'
    p = 3
    d = '7'
    n = n[:-p+1]
    if n[len(n)-1] <= 4:
        n[len(n)-1] = str((int(n[len(n)-1])+d)%10)
    for i in range(p-1):
        n = n+'0'
    print(n)
