# from collections import deque
import collections
class TreeNode:
    def __init__(self, val = 0, left= None, right = None):
        self.val = val
        self.left = left 
        self.right = right
class Solution :
    def levelOrder(self, root : TreeNode):
        res = []
        q = collections.deque()
        q.append(root)
        while q:
            qLen = len(q)
            level = []
            for i in range(qLen):
                node = q.popleft()
                if node: 
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            
            if level:
                res.append(level)
        return res
#create nodes
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)

root.left.left = None
root.left.right = None 

root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

sol = Solution()
output = sol.levelOrder(root)
print("the result of bfs is ",output)
