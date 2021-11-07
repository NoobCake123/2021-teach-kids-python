class arithmeticfuncs:
    def __init__(self, listonums):
        self.nums = listonums

    def apowb(self):
        if len(self.nums) == 2:
            final = pow(self.nums[0], self.nums[2])
        else:
            return "yeet"
        return final
    def sumonums(self):
        return sum(self.nums)
    def productonums(self):
        final = 1
        for i in self.nums:
            final = final*i
        return final



if __name__ == "__main__":
    pass
