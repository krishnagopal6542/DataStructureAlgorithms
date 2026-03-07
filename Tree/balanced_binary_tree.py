# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        Check if a binary tree is height-balanced.
        
        A height-balanced binary tree is defined as:
        A binary tree in which the left and right subtrees of every node 
        differ in height by no more than 1.
        
        Time Complexity: O(n) where n is the number of nodes
        Space Complexity: O(h) where h is the height of the tree (recursion stack)
        """
        def check_height(node):
            """
            Helper function that returns the height of the tree if balanced,
            or -1 if the tree is not balanced.
            
            This approach combines height calculation with balance checking
            in a single traversal for optimal efficiency.
            """
            # Base case: empty tree is balanced with height 0
            if not node:
                return 0
            
            # Check left subtree
            left_height = check_height(node.left)
            if left_height == -1:  # Left subtree is not balanced
                return -1
            
            # Check right subtree
            right_height = check_height(node.right)
            if right_height == -1:  # Right subtree is not balanced
                return -1
            
            # Check if current node is balanced
            if abs(left_height - right_height) > 1:
                return -1
            
            # Return height of current subtree
            return max(left_height, right_height) + 1
        
        # Tree is balanced if check_height doesn't return -1
        return check_height(root) != -1


# Example usage and test cases
def test_balanced_tree():
    """Test the balanced binary tree implementation"""
    solution = Solution()
    
    # Test case 1: Balanced tree [3,9,20,null,null,15,7]
    #       3
    #      / \
    #     9  20
    #       /  \
    #      15   7
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)
    
    print(f"Test 1 - Balanced tree: {solution.isBalanced(root1)}")  # Expected: True
    
    # Test case 2: Unbalanced tree [1,2,2,3,3,null,null,4,4]
    #          1
    #         / \
    #        2   2
    #       / \
    #      3   3
    #     / \
    #    4   4
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(2)
    root2.left.left = TreeNode(3)
    root2.left.right = TreeNode(3)
    root2.left.left.left = TreeNode(4)
    root2.left.left.right = TreeNode(4)
    
    print(f"Test 2 - Unbalanced tree: {solution.isBalanced(root2)}")  # Expected: False
    
    # Test case 3: Empty tree
    print(f"Test 3 - Empty tree: {solution.isBalanced(None)}")  # Expected: True
    
    # Test case 4: Single node
    root3 = TreeNode(1)
    print(f"Test 4 - Single node: {solution.isBalanced(root3)}")  # Expected: True
    
    # Test case 5: Only left child (unbalanced)
    root4 = TreeNode(1)
    root4.left = TreeNode(2)
    root4.left.left = TreeNode(3)
    print(f"Test 5 - Left skewed tree: {solution.isBalanced(root4)}")  # Expected: False


if __name__ == "__main__":
    test_balanced_tree()
