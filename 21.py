# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        cur_1 = list1
        cur_2 = list2

        merge = None
        cur_merge = None
        # compare cur1 to cur2 and set lower value, then make lower = lower.next
        # set lower to merge if null or merge.next
        # end when both cur1 and cur 2 = null

        while cur_1 or cur_2:
            lower = None
            if cur_1 == None:
                lower = cur_2
                cur_2 = cur_2.next
            elif cur_2 == None:
                lower = cur_1
                cur_1 = cur_1.next
            elif cur_1.val < cur_2.val:
                lower = cur_1
                cur_1 = cur_1.next
            elif cur_1.val > cur_2.val:
                lower = cur_2
                cur_2 = cur_2.next
            else:
                lower = cur_1
                cur_1 = cur_1.next

            if merge != None:
                cur_merge.next = lower
                cur_merge = cur_merge.next
            else:
                merge = lower
                cur_merge = merge


        return merge
