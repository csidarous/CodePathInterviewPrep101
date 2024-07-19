#Problem 1
def is_nested(paren_s):
  if paren_s == "":
    return True
  if len(paren_s) % 2 != 0 or len(paren_s) <= 1:
    return False
  if len(paren_s) >= 2 and paren_s[0] == "(" and paren_s[-1] == ")":
    return is_nested(paren_s[1:-1])
  else:
    return False

# input = "(())"
# input_2 = "((())))"
# print(is_nested(input_2))

#Problem 2
def count_ones(lst):
  left = 0
  right = len(lst) -1

  while left <= right:
    middle = (left + right) // 2
    if lst[middle] == 0:
      left = middle + 1
    else:
      right = middle - 1

  if lst[left] == 1:
    return len(lst) - left
  return 0


# Input= [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1]
# print(count_ones(Input))


#Problem 3

def binary_search(nums, target):
  return binary_search_helper(nums, target, 0, len(nums) -1)


def binary_search_helper(nums, target, low, high):
    middle = (low + high) // 2
    if low > high:
      return -1

    if target == nums[middle]:
      return middle
    elif nums[middle] < target:
      low = middle + 1
      return binary_search_helper(nums, target, low, high)
    else:
      high = middle - 1
      return binary_search_helper(nums, target, low, high)


nums = [1, 3, 5, 7, 9, 11, 13, 15] 
target = 10
print(binary_search(nums,target))