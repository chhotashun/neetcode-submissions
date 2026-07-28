# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # brute force makes sense use array to store linked list 
        # 1) use fast and slow to get middle of linked list (two halves)
        slow, fast = head, head.next 
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next
        # reversed second half of linked list as well 
        second = slow.next 
        prev = slow.next = None 
        while second:
            tmp = second.next 
            second.next = prev 
            prev = second
            second = tmp 
        # 3) -merging two halves 
        first, second = head, prev 
        while second:
            tmp1, tmp2 = first.next, second.next 
            first.next = second 
            second.next = tmp1 
            first, second = tmp1, tmp2 
        
        #print(dummy.val)