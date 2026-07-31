"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashmap = {None : None}
        curr = head
        while curr:
            copy = Node(curr.val)
            #print("copy node: ", copy.val)
            #print("curr node map: ", curr.val)
            print(f"hashmap[{curr.val}]: ", copy.val)
            hashmap[curr] = copy
            curr = curr.next
        curr = head 
        # this pass connect pointers 
        # use hashmap to get curr.next and curr.random 
        while curr:
            copy_node = hashmap[curr]
            copy_next = hashmap[curr.next]
            copy_random = hashmap[curr.random]
            copy_node.next = copy_next 
            copy_node.random = copy_random 
            curr = curr.next 
        return hashmap[head]

