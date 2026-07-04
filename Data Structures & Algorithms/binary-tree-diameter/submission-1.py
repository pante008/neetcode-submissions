# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    
        stack =[root]
        np ={None:(0,0)}

        while stack:
            node = stack[-1]
            if node.left and node.left not in np:
                stack.append(node.left)
            elif node.right and node.right not in np:
                stack.append(node.right)
            else:
                node = stack.pop()
                leftHeight, leftDiameter = np[node.left]
                rightHeight, rightDiameter = np[node.right]
                np[node] = (1+ max(leftHeight,rightHeight),max(leftHeight+rightHeight,leftDiameter,rightDiameter))
        return np[root][1]

        