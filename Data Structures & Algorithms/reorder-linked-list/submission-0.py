# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Step 1: find the middle
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # Split the list in two
        cut = slow.next      # save the back half
        slow.next = None     # front half now ends at slow

        # Step 2: reverse the back half in place
        prev = None
        curr = cut
        while curr:
            temp = curr.next   # save the rest before flipping
            curr.next = prev   # flip the arrow
            prev = curr        # move prev up
            curr = temp    # move curr up
        first = head 
        second = prev 
        while second: 
            bang = first.next
            boom = second.next 
            first.next = second 
            second.next = bang 
            first = bang
            second = boom
        # Step 3: merge (still to do)

            

