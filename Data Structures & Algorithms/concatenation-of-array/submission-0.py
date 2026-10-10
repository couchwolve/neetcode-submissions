class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        ans = [0] * len(nums) * 2

        for i,num in enumerate(ans):
            ans[i] =  nums[i%len(nums)]
        return ans
        
        