'''
反转链表核心就是遍历列表的过程中，将当前节点的next指针指向前一个节点，这样就可以将当前节点反转过来。
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
        pre = None
        cur = head
        
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        
        return pre