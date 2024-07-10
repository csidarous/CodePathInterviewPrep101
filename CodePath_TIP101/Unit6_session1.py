class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

#Problem 1
Node(4,Node(3,Node(2)))

#Problem 2
def count_element(head, val):
  count = 0 
  curr = head
  while curr:
    if curr.value == val:
      count +=1
    curr = curr.next

  return count


# head = Node(4,Node(1,Node(2, Node(1))))
# print(count_element(head, 1))

#Problem 3
def print_list(node):
  current = node
  while current:
      print(current.value, end=" -> " if current.next else "")
      current = current.next
  print()


# I have a bug! 
def remove_tail(head):
  if head is None: # If the list is empty, return None
      return None
  if head.next is None: # If there's only one node, removing it leaves the list empty
      return None 

# Start from the head and find the second-to-last node
  current = head
  while current.next.next: 
      current = current.next

  current.next = None # Remove the last node by setting second-to-last node to None
  return head

head = Node(4,Node(1,Node(2, Node(1))))
newhead = remove_tail(head)
print_list(newhead)