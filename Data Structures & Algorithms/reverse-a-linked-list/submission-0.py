class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        front = None          # fix 2: start with an empty new list
        curr = head

        while curr:           # fix 1: indented inside the method
            node = ListNode(curr.val)   # fix 3: copy the current node's value
            node.next = front
            front = node
            curr = curr.next  # fix 4: step forward last

        return front          # fix 6: front is the head of the reversed list