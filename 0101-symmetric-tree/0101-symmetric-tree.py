class Solution:
    def isMirror(self, t1, t2):
        if t1 is None and t2 is None:
            return True 
        if t1 is None or t2 is None:
            return False 

        return (t1.val == t2.val
                and self.isMirror(t1.left, t2.right)
                and self.isMirror(t1.right, t2.left)
               )
        
    def isSymmetric(self, root):
        if root is None:
            return True 
        return self.isMirror(root.left, root.right)