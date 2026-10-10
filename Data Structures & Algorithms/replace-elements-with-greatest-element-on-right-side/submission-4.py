class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        greatest_element = -1
        
        i = len(arr)-1

        while i >= 0:

            temp = arr[i]

            arr[i] = greatest_element

            greatest_element = max(temp,greatest_element)

            i-=1
        
        return arr
            

