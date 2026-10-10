class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        max_global = 0
        max_local = 0

        for num in nums:
            if num == 1:
                max_local += 1
            else:
                max_global = max(max_global,max_local)
                max_local = 0
        
        max_global = max(max_global,max_local)
        return max_global

        