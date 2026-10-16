# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        m1 = []
        m2 = []
        result = 0
        result2 = 0 

        while l1: 
            m1.append(l1.val)
            l1 = l1.next
        while l2:
            m2.append(l2.val)
            l2 = l2.next
        while m1 != []:
            num = m1.pop()
            result = result * 10 + num
        while m2 != []:
            num = m2.pop()
            result2 = result2 * 10 + num
        result = result + result2
        result = str(result)[::-1]
        head = ListNode(int(result[0]))
        current = head
        for digit in result[1:]:
            current.next = ListNode(int(digit))
            current = current.next
        
        return head


