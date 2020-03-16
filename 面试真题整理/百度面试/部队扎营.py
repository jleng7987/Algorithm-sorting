n,k=map(int,input().split())

class Bt:
    def __init__(self,root):
        self.key = root
        self.left = None
        self.right = None

def leaf(self, root):
    if root == None:
        return 0
    elif root.left == None and root.right == None:
        return 1
    else:
        return (self.leaf(root.left) + self.leaf(root.right))

