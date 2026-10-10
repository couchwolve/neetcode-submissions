class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        max_till_now = 0
        temp = 0

        for num in nums:
            if num == 1:
                temp+=1
            else:
                temp = 0
            
            if temp > max_till_now:
                max_till_now = temp

        return max_till_now
        