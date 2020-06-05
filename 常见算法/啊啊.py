class Node:
    def __init__(self, x):
        self.val = x
        self.next = None


def funzhuan(head):
    if head == None:
        return None
    L, M, R = None, None, head
    while R.next != None:
        L = M
        M = R
        R = R.next
        M.next = L
    R.next = M
    return R

def funzhuan2(head):
    if head.next == None:  # 递归停止的基线条件
        return head
    new_head = funzhuan2(head.next)
    head.next.next = head  # 当前层函数的head节点的后续节点指向当前head节点
    head.next = None  # 当前head节点指向None
    return new_head

if __name__ == '__main__':
    l1 = Node(3)
    l1.next = Node(2)
    l1.next.next = Node(1)
    l1.next.next.next = Node(9)
    # l = funzhuan(l1)
    l = funzhuan2(l1)
    print(l.val, l.next.val, l.next.next.val, l.next.next.next.val)
