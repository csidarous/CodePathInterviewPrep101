#Problem 1


#Understand
#Edge case 1:   root: 1  return True
#Edge false case 1:   root: 1, 2, 1 return false

#Plan
# check root to see if root and store that value
#recursively iterate through tree comparing each tree node vvaleu to the root


class TreeNode():
   def __init__(self, value, left=None, right=None):
       self.val = value
       self.left = left
       self.right = right

def is_univalued(root):
  if root is None:
    return False
  else:
    return is_univalued_rec(root, root.val)



def is_univalued_rec(node, val):
   if not node:
      return True
   if node.val != val:
      return False
   return is_univalued_rec(node.left, val) and is_univalued_rec(node.right, val)


# def binary(root, val):
#   if root is None:
#     return 
#   binary(root.left, root.val)
#   binary(root.right, root.val)



# input 1    
# #   1
#   1   1
#  1 1   1 
# 1 1        
input_1 = TreeNode(1, TreeNode(1, TreeNode(3), TreeNode(1)), TreeNode(1, TreeNode(1)))

#print(is_univalued(input_1))
# input 2
#     1 
#   1   2
# 1  1    1

# problem 2:

def height(root):
   if not root:
      return 0

   def find_max(node, counter):
      if not node:
         return counter
      return max(find_max(node.left, counter + 1), find_max(node.right, counter + 1))

   return find_max(root, 0)

print(height(input_1))


#Problem 3 

class TreeNode():
     def __init__(self, key, value, left=None, right=None):
         self.key = key
         self.val = value
         self.left = left
         self.right = right

def insert(root, key, value):

   if root is None:
       return TreeNode(key, value)

   if key > root.key:
      root.right = insert(root.right, key, value)
   elif key < root.key:
       root.left =  insert(root.left, key, value)
   else:
      root.val = value
   return root


def print_tree(node, level=0, prefix="Root: "):
    if node is not None:
        print(" " * (level * 4) + prefix + f"({node.key}, {node.val})")
        if node.left:
            print_tree(node.left, level + 1, "L--- ")
        if node.right:
            print_tree(node.right, level + 1, "R--- ")

# Test Input Tree #1
root1 = TreeNode(10, '')
root1.left = TreeNode(8, '')
root1.right = TreeNode(15, '')
root1.left.left = TreeNode(1, '')
root1.left.right = TreeNode(6, '')

print("Before Insertion:")
print_tree(root1)

root1 = insert(root1, 9, 'Naruto')

print("\nAfter Insertion:")
print_tree(root1)

# Test Input Tree #2 (Empty Tree)
root2 = None

print("\nBefore Insertion:")
print_tree(root2)

root2 = insert(root2, 4, 'Sailor Moon')

print("\nAfter Insertion:")
print_tree(root2)

#Problem 4
def remove_bst(root, key):
   if root is None:
      return

   if key > root.key:
      root.right = remove_bst(root.right, key)
   elif key < root.key:
       root.left =  remove_bst(root.left, key)
   else:
      if root.left is None:
         return root.right
      elif root.right is None:
         return root.left

      # Node with two children, get the in-order successor (smallest in the right subtree)
      temp_val = find_min(root.right)
      root.val = temp_val
      root.right = remove_bst(root.right, temp_val)

      return root

def find_min(node):
    """
    Find the smallest value in the BST.
    """
    current = node
    while current.left is not None:
        current = current.left
    return current.val