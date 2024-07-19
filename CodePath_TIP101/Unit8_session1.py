#Problem 1
class TreeNode:

  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


root = TreeNode(10, TreeNode(4), TreeNode(6))

#Problem 2 : 3-Node Sum

#U  Take in 3 nodes, 1 root , two children,
# return true if the sum of the values of the children is equal to the value of the root
#otherwise return false

#P
#sum = root.left.value + root.right.value
# if sum == root.value return true
#else return false

#I


def check_tree(root):
  sum = root.left.val + root.right.val
  if sum == root.val:
    return True
  else:
    return False


print(check_tree(root))


#Problem 3
def check_tree_2(root):
  if not root.left:
    root.left = TreeNode(0)

  if not root.right:
    root.right = TreeNode(0)

  sum = root.left.val + root.right.val
  if sum == root.val:
    return True
  else:
    return False


root = TreeNode(10, TreeNode(10))

# print(check_tree(root))
print(check_tree_2(root))

#Problem 4


def left_most(root):
  if root is None:
    return None

  if root.left is None:
    return root.val

  while root.left:
    root = root.left

  return root.val


root_1 = TreeNode(10, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2))

print(left_most(root_1))

root_2 = TreeNode(10)
print(left_most(root_2))

#Problem 5 : Find Leftmost Node II
#U Find the leftmost node in a binary tree, using recursion and return the value of the leftmost node.

#P if root.left == None return root.val
# else return left_most(root.left)

#I


def left_most_recurse(root):
  if root.left == None:
    return root.val
  else:
    return left_most_recurse(root.left)


print(left_most_recurse(root_1))
print(left_most_recurse(root_2))

# Problem 6: In-order Traversal
# Given the root of a binary tree, return a list representing the inorder traversal of its nodes' values. In an inorder traversal we traverse the left subtree, then the current node, then the right subtree.


def inorder_traversal(root):
  lst = []
  traverse(root, lst)
  return lst


def traverse(root, lst):
  if root is None:
    return

  traverse(root.left, lst)
  lst.append(root.val)
  traverse(root.right, lst)


print(inorder_traversal(root_1))

#Problem 7 

def size(root):
  if root is None:
    return 0

  l = 1 + size(root.left)
  size(root.left)
  size(root.right)

  return 

print(size(root_1))