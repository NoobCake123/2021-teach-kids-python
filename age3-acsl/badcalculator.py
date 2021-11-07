class operations:
    def __init__(self, nums):
        self.isit2 = True
        if len(nums) == 2:
            self.isit2 = True
            self.num1 = nums[0]
            self.num2 = nums[1]
        elif len(nums) >= 2:
            print("unfortunately my calculator does not work with more than 2 numbers")
        else:
            self.isit2 = False
            self.num1 = nums[0]

    def addition(self):
        return self.num1 + self.num2

    def subtraction(self):
        return self.num1 + self.num2

    def multiplication(self):
        return self.num1 * self.num2

    def division(self):
        return self.num1 / self.num2

    def exponent(self):
        return pow(self.num1, self.num2)

    def sqrt(self):
        if self.isit2 == False:
            return pow(self.num1, 0.5)
        else:
            return "use the root function"

    def root(self):
        return pow(self.num1, 1 / self.num2)
def extractdata(expression,listofops):
    for i in expression:





if __name__ == "__main__":
    op = ''
    listofops = []
    runningtotal = 0
    o = operations
    while expression != "stop":
        expression = list(input("please enter your expression like so: a+b with no spaces"))


