# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):

        self.good_nodes = 0
        def dfs(root, largest=float('-inf')):

            if root is None:
                return 
            
            if root.val >= largest:
                self.good_nodes += 1
            
            largest = max(largest, root.val)

            if root.left:
                dfs(root.left, largest)
            
            if root.right:
                dfs(root.right, largest)
        
        dfs(root)
        return self.good_nodes 


        