# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy 
        carry = 0
        while l1 or l2 or carry:
            t1 = l1.val if l1 else 0
            t2 = l2.val if l2 else 0
            print("t1 here: ", l1.val if l1 else None)
            print("t2 here: ", l2.val if l2 else None)
            total = t1 + t2 + carry
            carry = total // 10 # alternate carry, digit = divmod(total, 10) gives carry = total // 10 and digit = total % 10
            digit = total % 10
            tail.next = ListNode(digit)
            tail = tail.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next

