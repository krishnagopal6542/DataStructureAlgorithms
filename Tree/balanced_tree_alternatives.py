# Alternative approaches for checking if a binary tree is balanced
from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    # APPROACH 1: Top-down recursive (naive approach)
    # Time: O(n^2) in worst case, Space: O(h)
    def isBalanced_topdown(self, root: Optional[TreeNode]) -> bool:
        """
        Top-down approach: Check balance at each node by calculating heights.
        Less efficient but more intuitive.
        """
        def get_height(node):
            if not node:
                return 0
            return max(get_height(node.left), get_height(node.right)) + 1
        
        if not root:
            return True
        
        # Check if current node is balanced
        left_height = get_height(root.left)
        right_height = get_height(root.right)
        
        if abs(left_height - right_height) > 1:
            return False
        
        # Recursively check left and right subtrees
        return self.isBalanced_topdown(root.left) and self.isBalanced_topdown(root.right)
    
    
    # APPROACH 2: Bottom-up recursive (optimal - same as original)
    # Time: O(n), Space: O(h)
    def isBalanced_bottomup(self, root: Optional[TreeNode]) -> bool:
        """
        Bottom-up approach: Calculate height and check balance in single pass.
        Most efficient approach.
        """
        def check_balance(node):
            if not node:
                return 0, True  # (height, is_balanced)
            
            left_height, left_balanced = check_balance(node.left)
            if not left_balanced:
                return -1, False
            
            right_height, right_balanced = check_balance(node.right)
            if not right_balanced:
                return -1, False
            
            # Check current node balance
            if abs(left_height - right_height) > 1:
                return -1, False
            
            return max(left_height, right_height) + 1, True
        
        _, is_balanced = check_balance(root)
        return is_balanced
    
    
    # APPROACH 3: Iterative with explicit stack
    # Time: O(n), Space: O(n)
    def isBalanced_iterative(self, root: Optional[TreeNode]) -> bool:
        """
        Iterative approach using stack to simulate recursion.
        Good for avoiding recursion depth limits.
        """
        if not root:
            return True
        
        # Stack stores (node, height) pairs
        stack = [(root, 0)]
        heights = {}  # Cache heights to avoid recalculation
        
        def get_height(node):
            if not node:
                return 0
            if node in heights:
                return heights[node]
            
            # Use BFS to calculate height iteratively
            queue = deque([(node, 0)])
            max_depth = 0
            
            while queue:
                curr_node, depth = queue.popleft()
                max_depth = max(max_depth, depth)
                
                if curr_node.left:
                    queue.append((curr_node.left, depth + 1))
                if curr_node.right:
                    queue.append((curr_node.right, depth + 1))
            
            heights[node] = max_depth + 1
            return heights[node]
        
        # Check each node for balance
        visited = set()
        stack = [root]
        
        while stack:
            node = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            
            left_height = get_height(node.left)
            right_height = get_height(node.right)
            
            if abs(left_height - right_height) > 1:
                return False
            
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        
        return True
    
    
    # APPROACH 4: Using separate height function (cleaner but less efficient)
    # Time: O(n^2) worst case, Space: O(h)
    def isBalanced_separate_height(self, root: Optional[TreeNode]) -> bool:
        """
        Clean approach with separate height calculation function.
        More readable but less efficient due to repeated height calculations.
        """
        def height(node):
            """Calculate height of the tree rooted at node"""
            if not node:
                return 0
            return max(height(node.left), height(node.right)) + 1
        
        def is_balanced_helper(node):
            """Check if tree rooted at node is balanced"""
            if not node:
                return True
            
            # Check balance condition
            if abs(height(node.left) - height(node.right)) > 1:
                return False
            
            # Recursively check subtrees
            return is_balanced_helper(node.left) and is_balanced_helper(node.right)
        
        return is_balanced_helper(root)
    
    
    # APPROACH 5: Post-order traversal with early termination
    # Time: O(n), Space: O(h)
    def isBalanced_postorder(self, root: Optional[TreeNode]) -> bool:
        """
        Post-order traversal approach with early termination.
        Similar efficiency to bottom-up but different implementation style.
        """
        def postorder(node):
            # Returns height if balanced, -1 if not balanced
            if not node:
                return 0
            
            # Post-order: process children first
            left = postorder(node.left)
            if left == -1:  # Early termination
                return -1
            
            right = postorder(node.right)
            if right == -1:  # Early termination
                return -1
            
            # Process current node
            if abs(left - right) > 1:
                return -1
            
            return max(left, right) + 1
        
        return postorder(root) != -1


def create_test_trees():
    """Create test trees for comparison"""
    # Balanced tree
    balanced = TreeNode(3)
    balanced.left = TreeNode(9)
    balanced.right = TreeNode(20)
    balanced.right.left = TreeNode(15)
    balanced.right.right = TreeNode(7)
    
    # Unbalanced tree
    unbalanced = TreeNode(1)
    unbalanced.left = TreeNode(2)
    unbalanced.right = TreeNode(2)
    unbalanced.left.left = TreeNode(3)
    unbalanced.left.right = TreeNode(3)
    unbalanced.left.left.left = TreeNode(4)
    unbalanced.left.left.right = TreeNode(4)
    
    return balanced, unbalanced


def test_all_approaches():
    """Test all approaches and compare results"""
    solution = Solution()
    balanced_tree, unbalanced_tree = create_test_trees()
    
    approaches = [
        ("Top-down Recursive", solution.isBalanced_topdown),
        ("Bottom-up Recursive", solution.isBalanced_bottomup),
        ("Iterative", solution.isBalanced_iterative),
        ("Separate Height Function", solution.isBalanced_separate_height),
        ("Post-order Traversal", solution.isBalanced_postorder)
    ]
    
    print("=== PERFORMANCE COMPARISON ===\n")
    
    for name, method in approaches:
        print(f"{name}:")
        print(f"  Balanced tree: {method(balanced_tree)}")
        print(f"  Unbalanced tree: {method(unbalanced_tree)}")
        print(f"  Empty tree: {method(None)}")
        print()
    
    print("=== COMPLEXITY ANALYSIS ===")
    print("1. Top-down Recursive: O(n²) time, O(h) space - Simple but inefficient")
    print("2. Bottom-up Recursive: O(n) time, O(h) space - Most efficient")
    print("3. Iterative: O(n) time, O(n) space - Avoids recursion limits")
    print("4. Separate Height: O(n²) time, O(h) space - Most readable")
    print("5. Post-order: O(n) time, O(h) space - Clean recursive style")


if __name__ == "__main__":
    test_all_approaches()
