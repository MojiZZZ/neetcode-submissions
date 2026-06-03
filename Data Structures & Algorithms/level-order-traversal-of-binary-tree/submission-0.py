# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        answer = []
        if root:
            q.append(root)
            answer.append([root.val])
        while q:
            level_nodes = []
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    level_nodes.append(node.left.val)
                    q.append(node.left)

                if node.right:
                    level_nodes.append(node.right.val)
                    q.append(node.right)

            if level_nodes:    
                answer.append(level_nodes)
            print(answer)
        return answer
                
                


