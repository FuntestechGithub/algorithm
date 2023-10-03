'''
Leetcode 2095 https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/description/?envType=study-plan-v2&envId=leetcode-75
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head):
        '''
        fast slow pointer
        '''
        if head.next is None:
            return None

        slow, fast, pre = head, head, None

        while fast and fast.next:
            fast = fast.next.next
            pre = slow
            slow = slow.next
        
        # connect pre directly to slow
        pre.next = slow.next
        return head