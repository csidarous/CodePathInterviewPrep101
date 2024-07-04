#Problem 1
class Pokemon():
  def  __init__(self, name, hp, damage):
    self.name = name
    self.hp = hp # hit points
    self.damage = damage # The amount of damage this pokemon does to its opponent every attack

  def attack(self, opponent):
    opponent.hp -= self.damage
    if opponent.hp <= 0:
      opponent.hp = 0
      print(f'{opponent.name} fainted')
    else:
      print(f'{self.name} dealt {self.damage} damage to {opponent.name}')

# pikachu = Pokemon("Pikachu", 30, 20)
# bulbasaur = Pokemon("Bulbasaur", 20, 30) 

# opponent = bulbasaur
# pikachu.attack(opponent)

#Problem 2
class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

lst = ["Jigglypuff", "Wigglytuff",'chris']

# node_1 = Node(0)
# node_1.value = lst[0]
# node_2 = Node(0)
# node_2.value = lst[1]
# node_1.next = node_2

node_2 = Node(lst[1])
node_1 = Node(lst[0], node_2)

# print(node_1.value, "->", node_1.next.value)
# print(node_2.value, "->", node_2.next)

#Problem 3
def add_first(head, new_node):
  new_node.next = head
  return new_node

head = lst[0]
# print(node_1.value, "->", node_1.next.value)

# new_node = Node("Ditto")
# node_1 = add_first(node_1, new_node)

# print(node_1.value, "->", node_1.next.value)


#Problem 4
node_3 = Node(lst[2])
node_2 = Node(lst[1], node_3)
node_1 = Node(lst[0], node_2)

def get_tail(head):
  curr = head
  if head == None:
    return None
  while curr.next != None:
    curr = curr.next
  return curr.value

# head = node_1
# tail = get_tail(node_1)
# print(tail)

#Problem 5
def ll_replace(head, original, replacement):
  curr = head
  while curr != None:
    if curr.value == original:
      curr.value = replacement
    curr = curr.next

num3 = Node(5)
num2 = Node(6, num3)
num1 = Node(5, num2)
# initial linked list: 5 -> 6 -> 5

head = num1
ll_replace(head, 5, "banana")


# while head.next != None:
#   print(head.value)
#   head = head.next
# print(head.value)

#Problem 6
def listify_first_n(head, n):
  result = []
  curr = head
  count = 0

  while curr != None and count < n:
    result.append(curr.value)
    curr = curr.next
    count += 1

  return result

# linked list: a -> b -> c
#head = num1
lst = listify_first_n(head,2)
print(lst)

# linked list: j -> k -> l 
head2 = num2
lst2 = listify_first_n(head2,5)
print(lst2)

#much fun 