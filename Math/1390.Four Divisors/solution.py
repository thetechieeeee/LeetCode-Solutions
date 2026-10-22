class Solution:
    def sumFourDivisors(self, nums: list[int]) -> int:
        summ = 0
        for n in nums:
            total = 0
            count = 0
            i = 1
            while i * i <= n:
                if n % i == 0:
                    total += i
                    count += 1
                    if i != n // i:
                        total += n // i
                        count += 1
                i += 1
                if count > 4:
                    break
            if count == 4:
                summ += total
        return summ