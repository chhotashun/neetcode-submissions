# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # o(n) space and o(1) time 
        # get length of linked list 
        length = 0
        tmp = head 
        while tmp:
            length += 1
            tmp = tmp.next 
        # edge case 
        print(length)
        delete_node = length - n
        # edge case=
        if delete_node == 0:
            return head.next 
        counter = 0
        curr = head 
        prev = None 
        while counter < delete_node:
            counter += 1
            prev = curr
            curr = curr.next 
        prev.next = curr.next
        return head
