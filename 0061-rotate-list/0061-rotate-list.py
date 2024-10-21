# Definition for singly-linked list.
#class ListNode:
#    def __init__(self, val=0, next=None):
#        self.val = val
#        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: 
            return head

        temp = head
        lenght = 1
        while temp.next:
            temp = temp.next
            lenght+=1
        k = k % lenght
        if k == 0:
            return head
        curr = head
        for i in range(lenght - k - 1):
            curr = curr.next
        newHead = curr.next
        curr.next = None
        temp.next = head
        return newHead

        