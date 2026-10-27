class Solution:
    def addDigits(self, num: int) -> int:
        while num>=10:
            dig_sum = 0
            while num>0:
                dig = num%10
                dig_sum +=dig
                num//=10
            num =dig_sum
        return num