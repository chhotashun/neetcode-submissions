# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # brute force use hashset 
        hashset = set()
        curr = head 
        while curr:
            if curr in hashset:
                return True
            if curr:
                print("curr value: ", curr.val)
            hashset.add(curr)
            curr = curr.next
            if (curr):
                print("next curr value: ", curr.val)
        return False
            