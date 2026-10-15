# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        curr1, curr2 = list1,list2
        new_head = ListNode()
        temp_head = new_head

        while curr1 and curr2:

            if curr1.val < curr2.val:
                new_head.next = curr1
                curr1 = curr1.next
                
            else:
                new_head.next = curr2
                curr2 = curr2.next

            new_head = new_head.next
        
        if curr1:
            while curr1:
                new_head.next = curr1
                curr1 = curr1.next
                new_head = new_head.next
        if curr2:
            while curr2:
                new_head.next = curr2
                curr2 = curr2.next
                new_head = new_head.next
        return temp_head.next
