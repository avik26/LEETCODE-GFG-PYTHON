class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return None

        head.next = self.removeElements(head.next, val)
        return head if head.val != val else head.next
