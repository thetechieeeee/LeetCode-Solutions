class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        n = x
        l = []
        while x>0:
            temp = x%10
            l.append(temp)
            x = x//10
        sum1=sum(l)
        if n%sum1 == 0:
            return sum1
        else:
            return  -1