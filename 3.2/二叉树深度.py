# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 11:10:01 2020

@author: talen
"""

#方法一，层次遍历从上到下按层级遍历二叉树，
#有多少层即二叉树有多深

class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        root = pRoot
        if not root:
            return 0
        curLevelNodeList = [root]
        length = 0
        while curLevelNodeList:
            tempNodeList = [] 
            for node in curLevelNodeList:
                if node.left is not None:
                    tempNodeList.append(node.left)
                if node.right is not None:
                    tempNodeList.append(node.right)
            curLevelNodeList = tempNodeList
            length += 1
        return length
    
#方法二，递归，比较每一条路径的长短
class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        root = pRoot
        if not root:
            return 0
        left = self.TreeDepth(root.left)+1
        right = self.TreeDepth(root.right)+1
        
        return max(left, right)        
    