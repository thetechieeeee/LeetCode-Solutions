class Solution:
    def findLucky(self, arr: list[int]) -> int:
        freq = Counter(arr)
        for i in range(max(arr),0,-1):
            if freq[i]== i:
                return i 
        return -1
