def converter(line1):
    """
    wow! i made my orwn function AND it has a docstring!!!!!!!!
    :param line1:
    :return:
    """
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
        n = n + str((abs(int(pthdigit) - d)) % 10)
    for i in range(p - 1):
        n = n + '0'
    return n

if __name__ == '__main__':
    for i in range(5):
        print(f'{i+1}.{converter(input(f"{i+1}.").split(" "))}')

    