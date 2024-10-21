# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()  # Sonucu taşıyacak bir dummy node
        current = dummy  # Sonucu oluşturmak için pointer
        carry = 0  # Elde varsa onu tutacak
        
        while l1 or l2 or carry:  # Listeler bitene ve elde kalmayana kadar devam
            val1 = l1.val if l1 else 0  # l1'in değeri yoksa 0 al
            val2 = l2.val if l2 else 0  # l2'nin değeri yoksa 0 al
            summ = val1 + val2 + carry  # Toplam
            
            carry = summ // 10  # Elde
            current.next = ListNode(summ % 10)  # Yeni düğüm ekle
            current = current.next  # İlerle
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return dummy.next  # Sonuç dummy'den itibaren döndürülecek