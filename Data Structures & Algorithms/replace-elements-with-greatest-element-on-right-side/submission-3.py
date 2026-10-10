class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        greatest_element_till_now = -1

        for i in range(len(arr)-1, -1,-1):
            greatest_element_till_now,arr[i] = max(arr[i],greatest_element_till_now),greatest_element_till_now
        
        return arr
