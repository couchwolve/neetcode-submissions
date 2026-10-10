class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        is_duplicate = set()
        for num in nums:
            if num in is_duplicate:
                return True
            is_duplicate.add(num)
        
        return False

        