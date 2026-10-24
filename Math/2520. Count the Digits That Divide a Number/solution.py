class Solution:
    def countDigits(self, n: int) -> int:
        original_num = n
        cnt = 0
        while n > 0:
            temp = n%10
            if original_num%temp==0:
                cnt+=1
            n//=10
        return cnt
