# https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/555

def maxDepth(self, root: TreeNode) -> int:

    current_level = 0
    to_visit = [root] if root else []
    
    while len(to_visit) > 0:
        current_level += 1
        print("starting a new level")
        print(current_level)
        
        next_level = []
        for node in to_visit:
            if node.left: 
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        to_visit = next_level
        
    return current_level