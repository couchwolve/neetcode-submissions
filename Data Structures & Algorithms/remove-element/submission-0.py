class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        i,j = 0,0 

        while j < len(nums):

            if nums[j] != val:
                nums[i] = nums[j]
                j+=1
                i+=1
            else:
                j+=1
        return i
        