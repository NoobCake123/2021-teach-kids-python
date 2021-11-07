def iq(age, brainsize, amountoflettersinname):
    return age + brainsize + amountoflettersinname * 1000000000


davidage = 10
davidbrainsize = 1000
amountoflettersinname = 5
print(iq(davidage, davidbrainsize, amountoflettersinname))
johnage = 10
johnbrainsize = 999
jamountoflettersinname = 4
print(iq(johnage, johnbrainsize, jamountoflettersinname))


####################################################################
class IQ:
    def __init__(self, age, brainsize, aln):
        self.age = age
        self.brainsize = brainsize
        self.aln = aln

    def iq(self):
        return self.age + self.brainsize + self.aln


david = IQ(10, 694269429, 12)
print(david.iq())
john = IQ(10, 69699669, 1000)
print(john.iq())
