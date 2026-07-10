# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tmp = head 
        prev = None 
        while tmp:
            nxt = tmp.next 
            tmp.next = prev 
            prev = tmp
            tmp = nxt 
        head = prev 
        return head