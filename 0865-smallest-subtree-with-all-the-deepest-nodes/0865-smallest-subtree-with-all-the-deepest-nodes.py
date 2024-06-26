# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        depth = {None : -1}
        def dfs(node,parent = None):
            if node:
                depth[node] = depth[parent] + 1
                dfs(node.left,node)
                dfs(node.right,node)
        dfs(root)
        max_depth = max(depth.values())
        
        def answer(node):
            if not node or depth.get(node,None) == max_depth:
                return node
            l, r = answer(node.left), answer(node.right)
            return node if l and r else l or r
        return answer(root)
    