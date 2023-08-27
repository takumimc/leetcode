# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        visited = []
        cur = head
        while cur != None:
            if cur in visited:
                return True
            visited.append(cur)
            cur = cur.next
        return False

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        cur = head
        while cur != None:
            if cur.val == 'visited':
                return True
            cur.val = 'visited'
            cur = cur.next
        return False
