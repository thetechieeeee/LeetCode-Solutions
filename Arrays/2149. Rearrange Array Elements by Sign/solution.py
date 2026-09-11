class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l = [0]*n
        p_ind =0
        n_ind = 1
        for i in range(n):
            if nums[i]<0:
                l[n_ind] =nums[i]
                n_ind+=2
            else:
                l[p_ind] = nums[i]
                p_ind+=2
        return l