# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # brute force is create new nodes for each addition 
        dummy = ListNode() 
        tail = dummy 
        carry = 0
        total = 0
        # build problem assume first both lists are same length
        # while l1 and l2 should handle list of same length assumption 
        # if list is not same length then we check for another 
        while l1 or l2 or carry:
            d1 = l1.val if l1 else 0
            d2 = l2.val if l2 else 0
            total = d1 + d2 + carry 
            carry, digit = divmod(total, 10)
            tail.next = ListNode(digit)
            tail = tail.next 
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        # assume list is not even length then- 
        return dummy.next 
