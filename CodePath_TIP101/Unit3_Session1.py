##Problem 1
# def sum_of_number_strings(nums):
#   sum = 0
#   for n in nums:
#     sum += int(n)

#   return sum

# nums = ["10", "20", "30"]
# sum = sum_of_number_strings(nums)
# print(sum)


# def remove_duplicates(nums):
#   i=0
#   while i<len(nums)-1:
#     if nums[i] == nums[i+1]:
#       nums.pop(i)
#     else:
#       i += 1
#   return nums

# nums = [1,1,1,2,3,4,4,5,6,6]
# print(remove_duplicates(nums))


# def reverse_only_letters(s):
#   temp = []
#   for i in s:
#     if i.isalpha() == True:
#       temp.append(i)
#   # temp.reverse()
#   str = ""
#   tempIndex = len(temp) - 1
#   for i in range(len(s)):
#     if s[i].isalpha() == True:
#       str += temp[tempIndex]
#       tempIndex -=1
#     else:
#        str += s[i]
#   return str

# s = "a-bC-dEf-ghIj"
# reversed_s = reverse_only_letters(s)
# print(reversed_s)



# from typing import Counter


# def longest_uniform_substring(s):
#   stack = []
#   counter = 0
#   tracker = []
#   for let in s:
#     if let in stack:
#       counter+=1
#     else:
#       tracker.append(counter)
#       stack = []
#       counter = 0
#       stack.append(let)


#   return max(tracker)



# s1 = "aabbbbCdAA"
# l1 = longest_uniform_substring(s1)
# print(l1)

# s2 = "abcdef"
# l2 = longest_uniform_substring(s2)
# print(l2)


# word ="encourage"
# char={}
# for i in word:
#   if i not in char:
#     char[i]=1
#   else:
#     char[i]+=1
# char['e']+=2
# print(char['e'])

# def return_substrings(s):
#   all_sub = set()
#   recent = {s}

#   while recent:
#       tmp = set()
#       for word in recent:
#           for i in range(len(word)):
#               tmp.add(word[:i] + word[i + 1:])
#       all_sub.update(recent)
#       recent = tmp

#   return all_sub
# print(return_substrings('abc'))


# def ransom_note(message, magazine):
#   i=0
#   while i<len(magazine):
#       for word in magazine: 
#           for a in range(len(word)):
#               possible_word=word[:i]+word[i+1:]
#           if possible_word==message:
#               return True
#           else:
#               continue
#       i+=1
#   return False

# print(ransom_note('cba', 'abc'))

# def reverse_list(lst):
#   pointer_1=0
#   pointer_2=len(lst)-1
#   while pointer_1<pointer_2:
#     swap=lst[pointer_1]
#     lst[pointer_1]=lst[pointer_2]
#     lst[pointer_2]=swap
#     pointer_1+=1
#     pointer_2-=1
#   return lst
# print(reverse_list([1, 2, 3, 4, 5]))




# def first_palindrome(words):
#   for word in words:
#     if word[::-1]==word:
#       return word
#   return ""
# words = ["abc","car","ada","racecar","cool"]
# palindrome1 = first_palindrome(words)
# print(palindrome1)

# words2 = ["abc","racecar","cool"]
# palindrome2 = first_palindrome(words2)
# print(palindrome2)

# words3 = ["abc", "def", "ghi"]
# palindrome3 = first_palindrome(words3)
# print(palindrome3)

def sort_array_by_parity(nums):

  pointer_1=0
  pointer_2=len(nums)-1
  while pointer_1<pointer_2:
    if nums[pointer_2]%2 ==0:
      if nums[pointer_1]%2 != 0:
        swap=nums[pointer_1]
        nums[pointer_1]=nums[pointer_2]
        nums[pointer_2]=swap
        pointer_1+=1
        pointer_2-=1
      else:
        pointer_1+=1
    else:
      pointer_2-=1
  return nums

print(sort_array_by_parity([0]))




# def is_long_pressed(name, typed):
#   #typed[pointer_2] == name[pointer_1]
#    # pointer_2 += 1 untill typed[pointer_2] != name[pointer_1]
#   # then compare typed[pointer_2] and name[pointer_1] again
#   # if they are not equal, return false
#   # if pointer_2 and pointer 1 reach end, return true
#   pointer_1=0
#   pointer_2=0
#   while poninter_2 < len(typed):
#     if pointer_1<len(name) and name[pointer_1]==typed[pointer_2]:
#       pointer_2+=1


def is_long_pressed(name, typed):
  i, j = 0, 0  # Initialize pointers for name and typed

  while j < len(typed):
      if i < len(name) and name[i] == typed[j]:
          # If characters match, move both pointers
          i += 1
      elif j == 0 or typed[j] != typed[j - 1]:
          # If characters don't match and it's not a repeat of the previous char in typed
          return False
      # Always move the pointer in typed
      j += 1

  # Check if all characters in name were matched
  return i == len(name)

# Example Usage:
name1 = "alex"
typed1 = "aaleex"
print(is_long_pressed(name1, typed1))  # Output: True

name2 = "saeed"
typed2 = "ssaaedd"
print(is_long_pressed(name2, typed2))  # Output: False

name3 = "courtney"
typed3 = "courtney"
print(is_long_pressed(name3, typed3))  # Output: True
