# from collections import deque
# from typing import Optional, List 

# # Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution(object):

#     def rightSideView_BFS(self, root: Optional[TreeNode]) -> List[int]:
#         """
#         BFS (Level Order Traversal) approach for Right Side View.
#         """
#         if not root:
#             return []
        
#         queue = deque([root])
#         result = []

#         print("outside queue", queue, "result", result)


#         while queue:
#             print("-"*30)
#             level_size = len(queue)
#             print("level_size", level_size)
#             # The rightmost node of the current level will be found at the last iteration
#             # of this inner loop (i == level_size - 1).
#             for i in range(level_size):
#                 node = queue.popleft()
#                 print("i", i, "node", node)
                
#                 # If it's the rightmost element at this level
#                 if i == level_size - 1:
#                     result.append(node.val)
#                     print("result", result)
                
#                 if node.left:
#                     queue.append(node.left)
#                     print("append queue left", queue)
#                 if node.right:
#                     queue.append(node.right)
#                     print("append queue right", queue)
#         print("-"*30)
#         print(result)
#         return 
    
#     def rightSideView_DFS(self, root: Optional[TreeNode]) -> List[int]:
#         """
#         DFS (Depth-First Search) approach for Right Side View.
#         Prioritizes right child traversal.
#         """
#         right_side_view = []

#         def dfs(node, depth):
#             if not node:
#                 return

#             # If this is the first time we've visited this depth,
#             # this node is the rightmost for this level (due to right-first traversal).
#             if depth == len(right_side_view):
#                 right_side_view.append(node.val)

#             # Traverse right child first
#             dfs(node.right, depth + 1)
#             # Then traverse left child
#             dfs(node.left, depth + 1)

#         dfs(root, 0)
#         return right_side_view

#     def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
#         # to use DFS:
#         # return self.rightSideView_DFS(root)
#         # to use BFS:
#         return self.rightSideView_BFS(root)



# if __name__ == "__main__":
#     # Construct this tree:
#     #       1
#     #      / \
#     #     2   3
#     #      \    \
#     #       5    4

#     root = TreeNode(1)
#     root.left = TreeNode(2)
#     root.right = TreeNode(3)
#     root.left.right = TreeNode(5)
#     root.right.right = TreeNode(4)

#     sol = Solution()
#     result = sol.rightSideView(root)
#     print("Right side view:", result)

# # for _ in range(3):
# #     password = input("Try again: ")



# ####################################################################
# bst 530

from typing import Optional 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        min_diff = float('inf')
        prev_val = -float('inf')
        
        stack = []
        current = root
        print("-"*15, "outside loop", "-"*15)
        print("min_diff", min_diff, "prev_val", prev_val, "stack",  stack, "current", current)
        i=1
        while current or stack:
            # Go left as far as possible
            print("="*15, f"-1- while loop, {i} time", "="*15)
            while current:
                stack.append(current)
                current = current.left
                print("-"*15, "-2- while loop", "-"*15)
                print("stack",  [node.val for node in stack], "current", current.val if current else None)

            # Pop the current node (smallest unprocessed node)
            print("-"*15, "outside 2 while loop", "-"*15)
            print("stack",  [node.val for node in stack], "current", current.val if current else None, "prev_val", prev_val if prev_val else None, "min_diff", min_diff)
            current = stack.pop()
            
            # Process current node
            if prev_val != -float('inf'):
                min_diff = min(min_diff, current.val - prev_val)
            
            prev_val = current.val
            print("-"*15, "after pop and if", "-"*15)
            # Move to the right subtree
            current = current.right
            print("stack",  [node.val for node in stack], "current", current.val if current else None, "prev_val", prev_val if prev_val else None, "min_diff", min_diff)

            i+=1
            
        return min_diff
    


# Manually build the tree:
#         4
#        / \
#       2   6
#      / \
#     1   3

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

# Create instance of Solution and call the method
sol = Solution()
result = sol.getMinimumDifference(root)
print("Minimum Absolute Difference:", result)