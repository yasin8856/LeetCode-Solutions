#Definition for singly-linked list.
#class ListNode:
#   def __init__(self, val=0, next=None):
#        self.val = val
#        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        back, front = None, head
        while front:
            nxt = front.next
            front.next = back
            back = front
            front = nxt
        return back

            
            
        