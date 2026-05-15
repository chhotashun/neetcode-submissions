# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = ListNode()
        tail = dummy
        temp = head 
        counter = 0
        while (temp):
            counter += 1
            temp = temp.next 
        if (counter == 1):
            tail.next = head
            
        else:
            temp = head 
            current = head
            x = 0
            while (current):
                nxt = current.next 
                counter -= 1
                tracker = x
                if (tracker > counter):
                    tail.next = None
                    break
                while (tracker < counter):
                    tracker += 1
                    temp = temp.next 
                tail.next = current 
                tail = tail.next 
                tail.next = temp
                tail = tail.next 
                current = nxt 
                temp = nxt 
                x += 1
        

