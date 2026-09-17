class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        l = len(nums)
        mp = {}
        for n in nums:
            if n in mp:
                mp[n]+=1
            else:
                mp[n] = 1
        for n,cnt in mp.items():
            if cnt>l/2:
                return n
        return -1