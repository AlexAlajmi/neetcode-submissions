# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy

        # give fast a head start so there's an n-node gap between fast and slow
        for _ in range(n + 1):
            fast = fast.next

        # move both until fast runs off the end
        while fast is not None:
            slow = slow.next
            fast = fast.next

        # slow is right before the node to remove, so skip over it
        slow.next = slow.next.next

        return dummy.next