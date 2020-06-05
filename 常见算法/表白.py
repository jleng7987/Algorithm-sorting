#!/usr/bin/env python
# coding = utf-8
class ListNode(object):
    def __init__(self, x):
        self.data = x
        self.next = None

class Solustion(object):
    def reverseList(self,head):
        pre = head
        cur = head.next
        pre.next = None
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre

if __name__ == '__main__':
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    s = Solustion(head)
    root = s.reverseList(head)
    while root:
        print(root.data)
        root = root.next
