
#Problem 1
from collections import deque

class TreeNode:
  def __init__(self, value=0, left=None, right=None):
      self.val = value
      self.left = left
      self.right = right

def level_order(root):
  # If the tree is empty:
  # return an empty list
  if root is None:
    return []
  # Create an empty queue using deque
  queue = deque()
  # Create an empty list to store the explored nodes
  lst = []
  # Add the root to the queue
  queue.append(root)
  # While the queue is not empty:
  # Pop the next node off the queue (pop from the left side!)
  # Add the popped node to the list of explored nodes
  while queue:
    removed = queue.popleft()
    lst.append(removed.val)

  # Add each of the popped node's children to the end of the queue
  #if the left side is not none
    if removed.left:
      queue.append(removed.left)
  #if the right side is not none
    if removed.right:
      queue.append(removed.right)

  # Return the list of visited nodes
  return lst

'''
Example Input Tree:

      4
     / \
    2   6
   / \  
  1   3

Example Input: root = 4
Expected Output: [4, 2, 6, 1, 3]
Explanation: 
Level 1: Node 4
Level 2 (left to right): Node 2, Node 6
Level 3 (left to right): Node 1, Node 3

'''
one = TreeNode(1)
three = TreeNode(3)
# six = TreeNode(6)
two = TreeNode(2, one, three)
root = TreeNode(4, two)
print(level_order(root))

#Problem 2
def min_depth(root):
  if root is None:
    return 0
  left_height = min_depth(root.left)+1
  right_height = min_depth(root.right)+1
  return min(left_height, right_height)

print(min_depth(root))

#Problem 3

def level_difference(root):
  if root is None:
    return 0

  level = 0 
  summEven = 0
  Oddsum = 0
  queue = deque([root])

  while queue:
    level_size = len(queue)

    for i in range(level_size):
      removed = queue.popleft()

      if level % 2 == 0:
        summEven += root.val
      else:
        Oddsum += root.val

      if removed.left:
        queue.append(removed.left)
      #if the right side is not none
      if removed.right:
        queue.append(removed.right)

    level +=1

  return Oddsum - summEven





  # 1) If the tree is empty, return 0.
  # 2) Create an empty queue and add the root node with level 1.
  # 3) Initialize sums for odd and even levels to 0.
  # 4) While the queue is not empty:
  #     a) Get the number of nodes at the current level.
  #     b) For each node at the current level:
  #         i) Pop the node from the queue.
  #         ii) Add its value to the appropriate sum (odd or even) based on the current level.
  #         iii) Add the left and right children to the queue for the next level.
  #     c) Increment the level.
  # 5) Return the difference between the odd and even sums.

