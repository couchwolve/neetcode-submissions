class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        ans = 0
        temp = 0

        for i in nums:

            if i == 1:
                temp+=1
                continue
            
            ans = max(temp,ans)
            temp = 0
        ans = max(temp,ans)
        return ans