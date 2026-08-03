# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def leftnode(node):
            h1=0
            while node:
                h1+=1
                node=node.left
            return h1
        def rightnode(node):
            h2=0
            while node:
                h2+=1
                node=node.right
            return h2
        if not root:
            return 0
        lh=leftnode(root)
        rh=rightnode(root)
        if lh==rh:
            return (2**lh)-1
        return 1+self.countNodes(root.left)+self.countNodes(root.right)


