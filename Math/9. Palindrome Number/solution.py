class Solution:
    def isPalindrome(self, x: int) -> bool:
        original = x
        rev = 0
        if x<0:
            return False
        while x>0:
            temp = x%10
            rev =rev*10+temp
            x= x//10
        return rev == original