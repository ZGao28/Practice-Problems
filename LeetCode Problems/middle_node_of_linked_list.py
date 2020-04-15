# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        l, temp = 1, head
        while temp.next:
            temp = temp.next
            l += 1
        for i in range(l//2):
            head = head.next
        return head
