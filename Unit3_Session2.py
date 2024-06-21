# Problem 1: Sum of Strings
# Write a function sum_of_number_strings() that takes in a list of strings nums. Each string is a representations of integers. The function should return the sum of these strings as an integer.

# def sum_of_number_strings(nums):
#     pass
# Example Usage:

# nums = ["10", "20", "30"]
# sum = sum_of_number_strings(nums)
# print(sum)
# Example Output: 60

# Problem 2: Remove Duplicates
# Write a function remove_duplicates() that takes in a sorted list of integers nums as a parameter and removes all duplicates in the list. The function returns the modified list.

# def remove_duplicates(nums):
#     newList = []
#     for num in nums:
#         if num not in newList:
#             newList.append(num)
#     return newList

# Example Input:
# nums = [1, 1, 1, 2, 3, 4, 4, 5, 6, 6]
# print(remove_duplicates(nums))
# Example Output: no_dups = [1,2,3,4,5,6]

# 💡 Hint: While Loops

# Problem 3: Reverse Letters
# Write a function reverse_only_letters() that takes in a string s as a parameter. The function reverses the order of the letters in the string and returns the new string. Non-letter characters should remain in their original positions.

# def reverse_only_letters(s):
#     pass
# Example Usage:

# s = "a-bC-dEf-ghIj"
# reversed_s = reverse_only_letters(s)
# print(reversed_s)
# Example Output: j-Ih-gfE-dCba

# Problem 4: Longest Uniform Substring
# Write a function longest_uniform_substring() that takes in a string s and returns the length of the longest uniform substring. A uniform substring consists of a single repeated character.

# def longest_uniform_substring(s):
#     pass
# Example Usage:

# s1 = "aabbbbCdAA"
# l1 = longest_uniform_substring(s1)
# print(l1)

# s2 = "abcdef"
# l1 = longest_uniform_substring(s2)
# print(l2)
# Example Output:

# 4
# 1
# Problem 5: Teemo's Attack
# In the game League of Legends, Teemo attacks his enemy Ashe with poison arrows. Write a function find_poisoned_duration() that takes in two parameters: time_series (the time at which Teemo's attacks hits Ashe) and time_duration (the duration of the poisoning effect). The function returns the total time that Ashe is in a poisoned condition.

# time_series is a list of integers that represents the times at which Teemo attacks and makes Ashe poisoned for the exact time_duration.

# If Teemo hits Ashe while she is still poisoned, the poison's duration starts over. For example, if Teemo attacks at times 1 and 4 for 3 seconds, the states at each time would be:

# 1: attacked
# 2: in poison state
# 3: in poison state
# 4: attacked, poison duration resets to 3
# 5: in poison state
# 6: in poison state
# 7: in poison state
# 8: in normal state
# This means that the total time that Ashe is in a poisoned condition is 5.


# def find_poisoned_duration(time_series, duration):
#     damage = 0
#     # Edge Case for odd number of attacks
#     if len(time_series) % 2 == 1:
#         damage += 3

#     # Find total damage based on duration
#     for i in range(len(time_series) - 1):
#         # duration of poison state logicl
#         if time_series[i + 1] - time_series[i] > duration:
#             damage += duration
#         elif time_series[i + 1] - time_series[i] <= duration:
#             damage += time_series[i + 1] - time_series[i] - 1
#     return damage


# # Example Usage:

# time_series = [1, 4, 9]
# damage = find_poisoned_duration(time_series, 3)
# print(damage)
# Example Output: 8

# Problem 6: Sum Unique Elements
# Write a function sum_of_unique_elements() that takes in two lists of integers, lst1 and lst2, as parameters and returns the sum of the elements that are unique in lst1.

# An element is unique if:

# it appears exactly once in lst1
# it does not appear in lst2
def sum_of_unique_elements(lst1, lst2):
    sum = 0
    for i in range(len(lst1)-1):
        if lst1[i] != lst2:
            sum += lst1[i]
    return sum
# Example Usage:

lstA = [1, 2 ,3, 4]
lstB = [3, 4, 5, 6]
lstC = [7, 7, 7, 7]

sum1 = sum_of_unique_elements(lstA, lstB)
print(sum1)

sum2 = sum_of_unique_elements(lstC, lstB)
print(sum1)
# Example Output

# 3
# 0
