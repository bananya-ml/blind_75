'''
Given the head of a singly linked list, reverse the list, and return the reversed list.
'''
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
'''


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None

        return newHead
