#Problem 1
def repeat_hello(n):
  if n > 0:
    print("Hello")
    repeat_hello(n - 1)

#repeat_hello(5)

def repeat_hello_iterative(n):
  while n > 0:
    print("hello")
    n-=1



#problem 2
def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n-1)


#print(factorial(5))

#problem 3
def list_sum(lst):
  if not lst:
    return 0
  return lst[0]+list_sum(lst[1:])

lst = [1,2,3,4,5]
#print(list_sum(lst))

#Problem 4

def is_power_of_two(n):
  if n <= 1:
    return False
  if n == 2:
    return True

  return is_power_of_two(n/2)

#print(is_power_of_two(64))

#problem 5


def binary_search(lst, target):
  left = 0
  right = len(lst) - 1
  mid = 0
  while left <= right:
    mid = (right+left)//2
    if lst[mid] == target:
      return mid
    elif lst[mid] < target:
      left = mid + 1
    else:
      right = mid - 1

  return -1

# Example Input: 
lst = [1, 3, 5, 7, 9, 11, 13, 15]
target = 11
#print(binary_search(lst, target)) 

#problem 6
def find_last(lst, target):
  left = 0
  right = len(lst) - 1
  mid = 0
  index = -1
  while left <= right:
    mid = (right+left)//2
    if lst[mid] == target:
      left = mid+1
      index = mid
    elif lst[mid] < target:
      left = mid + 1
    else:
      right = mid - 1
  return index

lst = [1, 3, 5, 7, 9, 11, 11, 13, 15]
target = 11
#print(find_last(lst, target))


#Problem 7

def find_floor(lst, x):
  right = len(lst) - 1
  index = -1
  while right > 0:
    if lst[right] <= x:
      return right
    else:
      right-=1


lst = [1, 2, 8, 10, 11, 12, 19]
x = 5
#print(find_floor(lst,x))

#second solution 

def find_floor2(lst, x):
  left = 0
  right = len(lst) - 1
  mid = 0
  floor = None
  while left <= right:
    mid = (right+left)//2
    if lst[mid] <= x:
      index = lst[mid]
      left = mid + 1
    else:
      right = mid - 1
  return index

lst = [1, 2, 8, 10, 11, 12, 19]
x = 5

print(find_floor2(lst,x))