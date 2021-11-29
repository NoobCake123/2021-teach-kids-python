def gullivermilk(startcash):
    times = 0
    costofmilk = 7
    while startcash >= costofmilk:
        startcash = startcash/costofmilk
        times += startcash/costofmilk
        costofmilk = costofmilk * 2
    print(times)
gullivermilk(7000000)