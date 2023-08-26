# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None

        rev = None

        while second != None:
            tmp = second.next # 4 None
            second.next = rev # 3-> 3
            rev = second #3 4
            second = tmp # 4 None

        cur = head
        cur2 = rev
        while cur2 != None:
            tmp1 = cur.next
            tmp2 = cur2.next
            cur.next = cur2
            cur2.next = tmp1
            cur = tmp1
            cur2 = tmp2
