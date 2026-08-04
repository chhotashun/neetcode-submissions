# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # algorithm- 1) divide head into k sublists ]
        # 2) reverse sublists and link them 
        # time and space- ?? o(N) both as space would be o(n/k) for the total sublists we make 
        # 3) better would be to reverse k lists in place and point the reversed tail to the node original tail pointed to.
        # Ex- 1->2->3->4 reversed = 3->2->1 4 store 4 in a nxt_tmp and 3->2->1->4 and proceed 
        # lets just do brute force 
        # divide head into k sublists and proceed 
        if not head:
            return None
        lst = []
        curr = head
        while curr:
            lst.append(curr)
            curr = curr.next
        for item in range(0, len(lst), k):
            if item + k <= len(lst):
                lst[item:item+k] = lst[item:item+k][::-1]
        for item in range(len(lst) - 1):
            lst[item].next = lst[item+1]
        lst[-1].next = None
        return lst[0]