from collections import deque
from typing import Optional, List 

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):

    def rightSideView_BFS(self, root: Optional[TreeNode]) -> List[int]:
        """
        BFS (Level Order Traversal) approach for Right Side View.
        """
        if not root:
            return []
        
        queue = deque([root])
        result = []

        print("outside queue", queue, "result", result)


        while queue:
            print("-"*30)
            level_size = len(queue)
            print("level_size", level_size)
            # The rightmost node of the current level will be found at the last iteration
            # of this inner loop (i == level_size - 1).
            for i in range(level_size):
                node = queue.popleft()
                print("i", i, "node", node)
                
                # If it's the rightmost element at this level
                if i == level_size - 1:
                    result.append(node.val)
                    print("result", result)
                
                if node.left:
                    queue.append(node.left)
                    print("append queue left", queue)
                if node.right:
                    queue.append(node.right)
                    print("append queue right", queue)
        print("-"*30)
        print(result)
        return 
    
    def rightSideView_DFS(self, root: Optional[TreeNode]) -> List[int]:
        """
        DFS (Depth-First Search) approach for Right Side View.
        Prioritizes right child traversal.
        """
        right_side_view = []

        def dfs(node, depth):
            if not node:
                return

            # If this is the first time we've visited this depth,
            # this node is the rightmost for this level (due to right-first traversal).
            if depth == len(right_side_view):
                right_side_view.append(node.val)

            # Traverse right child first
            dfs(node.right, depth + 1)
            # Then traverse left child
            dfs(node.left, depth + 1)

        dfs(root, 0)
        return right_side_view

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # to use DFS:
        # return self.rightSideView_DFS(root)
        # to use BFS:
        return self.rightSideView_BFS(root)



if __name__ == "__main__":
    # Construct this tree:
    #       1
    #      / \
    #     2   3
    #      \    \
    #       5    4

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(4)

    sol = Solution()
    result = sol.rightSideView(root)
    print("Right side view:", result)

# for _ in range(3):
#     password = input("Try again: ")
