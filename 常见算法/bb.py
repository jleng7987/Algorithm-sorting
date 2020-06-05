class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def max_sum(self, root, Sum):
    if root == None:
        return self.max_value
    if (root.left != None) & (root.right != None):
        self.max_sum(root.left, Sum + root.value)
        self.max_sum(root.right, Sum + root.value)
    elif (root.left != None) & (root.right == None):
        self.max_sum(root.left, Sum + root.value)
    elif (root.left == None) & (root.right != None):
        self.max_sum(root.right, Sum + root.value)
    else:
        if (Sum + root.value) > self.max_value:
            self.max_value = Sum + root.value