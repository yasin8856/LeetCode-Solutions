#Definition for singly-linked list.
#class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        faster = ListNode()
        slower = ListNode()
        faster.next = head
        slower.next = head
        while faster and faster.next:
            faster = faster.next.next
            slower = slower.next
            if faster == slower:
                return True
        return False