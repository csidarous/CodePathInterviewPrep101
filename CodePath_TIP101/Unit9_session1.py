#Unit 9 Session 1 

#Problem 1

# check for node left and right return false
# check for left.val == right.val return true or continue
# Travel node 
from typing import Deque


class TreeNode:
  def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right


def is_symmetric(root):
  if not root:
    return True

  #create an empty que 

  queue = Deque([(root.left,root.right)])

  while queue:
    left, right = queue.popleft()
    if not left and not right:
      continue
    if not left or not right:
      return False
    if left.val != right.val:
      return False

    queue.append((left.left, right.right))
    queue.append((left.right, right.left))
  return True


#     1        que[2,2]
#   /   \
#  2     2    que[3,3, 4,4]
# /  \   / \
# 3  4   4  3   que[4,4, none, none, none, none]
# que[none, none, none, none] empty
#return true


root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(2)
root1.left.left = TreeNode(3)
root1.left.right = TreeNode(4)
root1.right.left = TreeNode(4)
root1.right.right = TreeNode(3)
print(is_symmetric(root1))
# Test Case 2: Asymmetric Tree
root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(2)
root2.left.left = TreeNode(3)
root2.left.right = TreeNode(4)
root2.right.left = TreeNode(3)
root2.right.right = TreeNode(5)
print(is_symmetric(root2))