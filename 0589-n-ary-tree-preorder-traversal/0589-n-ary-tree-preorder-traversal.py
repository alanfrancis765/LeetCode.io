"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        result = []
        def dfs(root):

            if root is None:
                return 
            
            result.append(root.val)
            for child in root.children:
                dfs(child)
        dfs(root)
        return result 