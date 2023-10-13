# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # Function to get the length of a linked list
        def getLength(node):
            length = 0
            while node:
                length += 1
                node = node.next
            return length
        
        # Find the lengths and tail nodes of both linked lists
        lenA, lenB = getLength(headA), getLength(headB)
        tailA, tailB = headA, headB
        while tailA and tailA.next:
            tailA = tailA.next
        while tailB and tailB.next:
            tailB = tailB.next
        
        # If the tail nodes are different, there's no intersection
        if tailA != tailB:
            return None
        
        # Reset pointers to the heads
        ptrA, ptrB = headA, headB
        
        # Move the pointer of the longer linked list ahead
        if lenA > lenB:
            for _ in range(lenA - lenB):
                ptrA = ptrA.next
        else:
            for _ in range(lenB - lenA):
                ptrB = ptrB.next
        
        # Move both pointers until they meet at the intersection
        while ptrA != ptrB:
            ptrA = ptrA.next
            ptrB = ptrB.next
        
        return ptrA
