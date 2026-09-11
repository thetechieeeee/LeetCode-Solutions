class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n =len(nums)
        f = [0]*(n+1)
        for i in nums:
            if f[i]==0:
                f[i]+=1
            else:
                return i
        return 0