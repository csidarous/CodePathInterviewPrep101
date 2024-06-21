

#Problem 1
# def is_prime(n):
#   if n==1 or n==2:
#     return True
#   elif n%2==0:
#     return False
#   else:
#     for i in range(3,n//2+1,2):
#       if n%i==0:
#         return False
#   return True
# print(is_prime(5))
# print(is_prime(12))
# print(is_prime(9))

# ##Problem 2

# def reverse_list(lst):
#   front = 0
#   end = len(lst) - 1
#   rev = []
#   while front <= end:
#     rev.append(lst[end])
#     end-=1

#   return rev

# # nlst = [1, 2, 3, 4, 5]

# # print(reverse_list(nlst))

#problem 3

# def sort_array_by_parity(nums):
#   beginning = 0
#   end = len(nums)-1


#   while end > beginning:
#     if nums[end] % 2 == 0:
#       while nums[beginning] % 2 == 0:
#         beginning +=1
#       temp = nums[beginning]
#       nums[beginning] = nums[end]
#       nums[end] = temp
#     end -= 1

#   return nums

# nums = [3,1,2,4, 6,5,1,8]
# nums2 = [0]
# print(sort_array_by_parity(nums))
# print(sort_array_by_parity(nums2))



# def swap_fun(word):
#   pointer_1=0
#   pointer_2=len(word)-1
#   while pointer_1< pointer_2:
#     temp=word[]

def first_palindrome(words):
  for word in words:
    if word[::-1]==word:
      return word
  return ""

words = ["abc","car","ada","racecar","cool"]
palindrome1 = first_palindrome(words)
print(palindrome1)

words2 = ["abc","racecar","cool"]
palindrome2 = first_palindrome(words2)
print(palindrome2)

words3 = ["abc", "def", "ghi"]
palindrome3 = first_palindrome(words3)
print(palindrome3)

