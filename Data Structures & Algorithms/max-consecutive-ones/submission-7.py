class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        max_till_now = 0
        temp = 0

        for num in nums:
            
            temp = temp + 1 if num else 0
            
            max_till_now = max(temp,max_till_now)

        return max_till_now
        