class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        global_max,local_max = 0,0

        for num in nums:

            if num != 1:
                global_max = max(local_max,global_max)
                local_max = 0            
            else:
                local_max+=1
        
        global_max = max(local_max,global_max)
        return global_max

        