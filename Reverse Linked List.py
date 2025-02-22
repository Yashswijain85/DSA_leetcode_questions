# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Time Complexity --> O(n)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None 
        curr = head 
        nextPtr = None 

        while curr:
            nextPtr = curr.next
            curr.next = prev 
            prev = curr
            curr = nextPtr
        head = prev 
        return head
        
