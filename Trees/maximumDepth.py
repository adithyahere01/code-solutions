#Given the root of a binary tree, return its maximum depth.

 def maxDepth(self, root: Optional[TreeNode]) -> int:
        def maxNodes(node,sum):
            if not node:
                return sum
            return max(maxNodes(node.left,sum+1),maxNodes(node.right,sum+1))
        
        return maxNodes(root,0)
