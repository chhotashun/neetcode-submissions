# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp, count = head, 0
        while (temp):
            count += 1
            temp = temp.next
        if (count == 1):
            head = None
            return head
        node_del = count - n 
        if (node_del == 0):
            head = head.next 
            return head 
        loop_counter = 0
        prev = None 
        temp = head
        nxt = temp.next 
        while (loop_counter < node_del):
            prev = temp 
            temp = temp.next 
            nxt = temp.next 
            loop_counter += 1
        prev.next = nxt 
        return head