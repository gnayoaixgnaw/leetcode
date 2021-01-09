# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode()
        cursor = res
        
        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            #new digit
            val = val1+val2+carry
            carry = val//10
            val = val%10
            
            cursor.next = ListNode(val)
            #update cursor
            cursor = cursor.next
            l1 = l1.next if l1 else 0 
            l2 = l2.next if l2 else 0
            
        return res.next
