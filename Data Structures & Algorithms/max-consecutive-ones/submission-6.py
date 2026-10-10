class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        max_till_now = 0
        temp = 0

        for num in nums:
            
            temp = temp + 1 if num else 0
            
            if temp > max_till_now:
                max_till_now = temp

        return max_till_now
        